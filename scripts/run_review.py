#!/usr/bin/env python3
"""Multi-agent AI review pipeline for HTAN LinkML schema PRs.

Three specialized reviewers (structural, biological, coverage) run in parallel,
then a synthesis agent produces the final structured review.

Usage:
    python scripts/run_review.py \
        --diff /tmp/pr.diff \
        --meta /tmp/pr_meta.json \
        --rules .claude/skills/review-schema-pr/SKILL.md \
        --full-files /tmp/full_files/ \
        --out /tmp/review_output.md

    # Dry-run (writes prompts to /tmp/ without API calls):
    python scripts/run_review.py \
        --diff /tmp/pr.diff \
        --meta /tmp/pr_meta.json \
        --rules .claude/skills/review-schema-pr/SKILL.md \
        --full-files /tmp/full_files/ \
        --out /tmp/review_output.md \
        --dry-run
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_MODEL = "claude-sonnet-4-6"
REVIEWER_MAX_TOKENS = 2048
SYNTHESIS_MAX_TOKENS = 4096
MAX_DIFF_CHARS = 80_000       # ~20k tokens
MAX_FULL_FILES_CHARS = 60_000  # ~15k tokens

SKIP_PREFIXES = [
    "src/htan_",       # generated Python datamodels
    "JSON_Schemas/",   # generated JSON schemas
]

# ---------------------------------------------------------------------------
# Shared prompt fragments
# ---------------------------------------------------------------------------

CHANGES_ONLY_CONSTRAINT = """\
CRITICAL SCOPE RULE: You MUST only flag issues that are directly related to
content CHANGED in this PR. If an untouched area of the model has an issue,
DO NOT report it — that is out of scope for this review. Use the diff to
determine what changed, and the full files only to verify context around those
changes (e.g., inheritance chains, enum ordering, slot completeness in the
same class). Never audit unchanged schema content."""

CANONICAL_EXAMPLES = """\
## Canonical Examples (from this repo)

**Inheritance chain** (Sequencing / WES):
```
CoreFileAttributes
  └─ BaseSequencingAttributes         (is_a: CoreFileAttributes)
       └─ BaseSequencingLevel1Attributes (is_a: BaseSequencingAttributes)
            └─ BaseSequencingLevel2Attributes (is_a: BaseSequencingLevel1Attributes)
                 └─ BaseSequencingLevel3Attributes (is_a: BaseSequencingLevel2Attributes)
                      └─ BulkWESLevel3             (is_a: BaseSequencingLevel3Attributes)

Same chain for scRNA-seq: scRNALevel1 → Level2 → Level3and4.
No level may skip (e.g., BulkWESLevel3 is_a BaseSequencingLevel2Attributes is WRONG).
```

**Correct slot** (WES level_1.yaml):
```yaml
READ_LENGTH:
  range: integer
  required: true
  title: "Read Length"
  description: Read length in base pairs
```

**Correct enum** (sequencing.yaml):
```yaml
LibraryLayoutEnum:
  permissible_values:
    "Paired-end":
      description: Paired-end sequencing
    "Single-end":
      description: Single-end sequencing
```

**Correct identifier** (core.yaml):
```yaml
HTAN_DATA_FILE_ID:
  identifier: true
  range: string
  required: true
  pattern: "^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(D[0-9]{1,20})$"
  title: "HTAN Data File ID"
  description: HTAN-wide unique identifier for this data file
```

**Modules**: Biospecimen | Clinical | CoreFile | DigitalPathology | Imaging | \
MultiplexMicroscopy | scRNA-seq | Sequencing | SpatialOmics | WES"""

HARD_CONSTRAINTS = """\
## Hard Constraints

- Do NOT flag missing src/*/datamodel/*.py or JSON_Schemas/*.json unless the PR
  description explicitly claims they were regenerated.
- Do NOT flag YAML indentation style.
- Do NOT flag slot ordering within a class (only enum values must be alphabetical).
- Do NOT comment on test verbosity or structure.
- Do NOT invent severity labels. Use ONLY: [BLOCKING], [WARNING], [INFO].
- Do NOT hallucinate slot names, class names, or enum values not present in the diff.
- Do NOT flag issues in unchanged content — only review what the PR changes.
- If uncertain whether a violation exists, say so explicitly rather than guessing."""

REVIEWER_OUTPUT_FORMAT = """\
## Output Format

For each issue found, use this format:

[SEVERITY] `filename`: Short title
Explanation: 2-3 sentences on what is wrong, why it matters, and how to fix it.

Where SEVERITY is one of: BLOCKING, WARNING, INFO

If no issues found in your domain, output:
No issues found.

Do NOT produce a verdict, table, or final summary — the synthesis agent handles that."""

# ---------------------------------------------------------------------------
# Reviewer-specific prompts
# ---------------------------------------------------------------------------

STRUCTURAL_PERSONA = """\
You are a LinkML schema specialist reviewing a pull request to the HTAN data model.

Your focus is exclusively on LinkML structural correctness:
- Inheritance chains (`is_a`) — verify no levels are skipped
- Slot completeness — every slot must have `range`, `title`, `description`
- `required: true` annotations — verify intent
- `inlined`/`inlined_as_list` on slots whose range has `identifier: true`
- Enum integrity — alphabetical ordering, descriptions on every value, no duplicates
- Generated artifacts — only flag if PR claims to include them but they're missing

You are NOT reviewing biological correctness or test coverage — other reviewers handle those."""

BIOLOGICAL_PERSONA = """\
You are a cancer biologist and ontology specialist reviewing a pull request to the HTAN data model.

Your focus is exclusively on scientific and ontological correctness of CHANGED content:
- Provenance chains — new assay-level classes must link to biospecimen via HTAN_BIOSPECIMEN_ID or HTAN_PARENT_ID
- Ontology alignment — new disease/anatomy/treatment slots should reference NCIT, UBERON, or MONDO
- Wet-lab nuance — new assay classes in MultiplexMicroscopy, SpatialOmics, scRNA-seq, or
  DigitalPathology should have dedicated parameter slots
- Cardinality — `multivalued: true` on logically-singular slots; `required: true` newly
  added on clinical slots routinely absent in practice
- Enum exclusivity — overlapping permissible values (e.g., "Adenocarcinoma" vs "Adenocarcinoma, NOS")

You are NOT reviewing LinkML syntax or test coverage — other reviewers handle those."""

COVERAGE_PERSONA = """\
You are a test coverage and dependency specialist reviewing a pull request to the HTAN data model.

Your focus is exclusively on:
- Test coverage for CHANGED content:
  - New classes: tests for existence, is_a, required/optional slots, valid/invalid instances
  - New required slots: test data updated, slot marked required
  - New enums: valid/invalid value tests
  - New modules: test_<module>.py exists with full coverage
- Dependency versions:
  - LinkML pin in pyproject.toml — note if >2 minor versions behind stable
  - Deprecated LinkML API usage (dataclass_extensions_376, dataclasses_init_fn_with_kwargs)
- Schema version — note if substantial changes warrant a version bump
- Identifier strategy — new `identifier: true` slots MUST have a `pattern:` regex
- Slot overloading — generic names (type, value, status, code, result) without module prefix
- Unit consistency — physical-quantity slots lacking unit_of_measurement (_DAYS suffix exempt)

You are NOT reviewing LinkML syntax or biological correctness — other reviewers handle those."""

SYNTHESIS_PERSONA = """\
You are the senior reviewer synthesizing three specialized review outputs into the final
structured review for an HTAN data model pull request.

You receive outputs from:
1. **Structural reviewer** — LinkML syntax, inheritance, inlining, slot completeness, enums
2. **Biological reviewer** — ontology alignment, provenance, wet-lab nuance, cardinality
3. **Coverage reviewer** — test coverage, dependencies, identifier strategy, consistency

Your job:
- Deduplicate findings across reviewers
- Resolve any conflicts (structural reviewer's judgement takes precedence for LinkML issues)
- Produce the final structured output in the required format
- Set verdict to REQUEST_CHANGES if any [BLOCKING] issue exists, APPROVE otherwise
- Do NOT add new findings — only synthesize what the reviewers reported"""

OUTPUT_FORMAT = """\
## Required Output Format

A single verdict alert at the top, then a checklist table, then findings grouped
by severity in collapsible sections. Each finding appears EXACTLY ONCE — deduplicate
aggressively across reviewers and attribute with a parenthetical.

```markdown
> [!CAUTION]
> **N blocking issues must be resolved before merge**

OR (if no blocking issues and no warnings):

> [!TIP]
> All checklist items pass — no issues found.

OR (if warnings but no blocking):

> [!WARNING]
> **N warnings to address (no blocking issues)**

### Files Changed
- list each .yaml file in the diff

### Checklist Results

| Check | Result | Notes |
|---|---|---|
| Inheritance correctness | PASS / FAIL / N/A | ... |
| Inlining of nested objects | PASS / FAIL / N/A | ... |
| Slot completeness (range, title, description) | PASS / FAIL / N/A | ... |
| Enum integrity (alphabetical, descriptions) | PASS / FAIL / N/A | ... |
| Generated artifacts | PASS / FAIL / N/A | ... |

### Findings

Group by severity under headings. Each finding uses a GitHub task checkbox.
Blocking and warning findings use unchecked boxes (action needed by author).
Informational findings use checked boxes (no action needed).

If multiple reviewers flagged the same underlying issue, MERGE into one entry.
Add a parenthetical noting which reviewer(s) caught it.

#### Blocking

- [ ] **`filename` — Short title** *(structural)*
  Explanation of what is wrong, why it matters, and how to fix it.

- [ ] **`filename` — Short title** *(structural + biological)*
  Merged explanation covering both reviewers' perspectives.

#### Warnings

- [ ] **`filename` — Short title** *(coverage)*
  Explanation and suggested action.

#### Informational

- [x] **`filename` — Short title** *(coverage)*
  Context for awareness. No action needed.

Omit a severity section entirely if there are no findings at that level.

### Verdict
APPROVE or REQUEST_CHANGES
```"""

TASK_STEPS = """\
## Instructions

1. Read all three reviewer outputs carefully.
2. DEDUPLICATE AGGRESSIVELY: if two or three reviewers flagged the same underlying
   issue (even with different wording), merge into ONE bullet. Use the best
   explanation across all reviewers. Attribute with parenthetical, e.g.,
   *(structural + biological)*.
3. Resolve conflicts: structural reviewer takes precedence on LinkML issues.
4. Count unique findings per severity after deduplication.
5. Start with a single friendly, human sentence summarizing what you found.
   Examples:
   - "Looks good overall — just a few slot completeness issues to clean up before merge."
   - "Nice work on the new enum values! Found some blocking issues with slot definitions that need attention."
   - "This is a clean PR — all checks pass."
   Vary the tone naturally. Do NOT be robotic or use boilerplate.
6. Follow with the verdict alert (CAUTION if blocking, WARNING if only warnings,
   TIP if all clear).
7. Fill in the Checklist Results table — state PASS, FAIL, or N/A for each.
8. Group findings under severity headings (#### Blocking, #### Warnings,
   #### Informational). Use GitHub task checkboxes: `- [ ]` for blocking and
   warnings (action needed), `- [x]` for informational (no action needed).
   Each item has a bold title, 2-3 sentence explanation, and reviewer attribution.
   Write like a senior reviewer helping a colleague — direct but helpful.
9. Omit a severity heading if there are no findings at that level.
10. Set Verdict to REQUEST_CHANGES if any blocking issue exists, APPROVE otherwise.
11. Never omit the Verdict line.

CRITICAL: The final output must have NO duplicate findings. If you see the same
slot or enum issue mentioned by multiple reviewers, it is ONE finding, not three."""


# ---------------------------------------------------------------------------
# Diff filtering
# ---------------------------------------------------------------------------

def filter_diff(raw_diff: str) -> tuple[str, int]:
    """Remove generated-file hunks from the diff and cap total size."""
    sections: list[str] = []
    current: list[str] = []
    skip = False

    for line in raw_diff.splitlines(keepends=True):
        if line.startswith("diff --git"):
            if current and not skip:
                sections.append("".join(current))
            current = [line]
            skip = any(p in line for p in SKIP_PREFIXES)
        else:
            current.append(line)

    if current and not skip:
        sections.append("".join(current))

    diff = "".join(sections)
    skipped_chars = len(raw_diff) - len(diff)

    if len(diff) > MAX_DIFF_CHARS:
        diff = diff[:MAX_DIFF_CHARS] + "\n\n[diff truncated]"

    return diff, skipped_chars


# ---------------------------------------------------------------------------
# Full file loading
# ---------------------------------------------------------------------------

def load_full_files(full_files_dir: str | None) -> str:
    """Load full YAML file contents, prioritizing smaller files, up to char cap."""
    if not full_files_dir or not Path(full_files_dir).is_dir():
        return ""

    files = sorted(
        Path(full_files_dir).glob("*.yaml"),
        key=lambda p: p.stat().st_size,  # smaller files first
    )

    parts: list[str] = []
    total = 0

    for f in files:
        content = f.read_text()
        if total + len(content) > MAX_FULL_FILES_CHARS:
            remaining = MAX_FULL_FILES_CHARS - total
            if remaining > 500:  # include partial if meaningful
                parts.append(f"--- {f.name} (truncated) ---\n{content[:remaining]}\n[truncated]")
            parts.append(f"\n[Remaining files omitted — {MAX_FULL_FILES_CHARS:,} char cap reached]")
            break
        parts.append(f"--- {f.name} ---\n{content}")
        total += len(content)

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Rules loading (with frontmatter stripping)
# ---------------------------------------------------------------------------

def load_rules(rules_path: str) -> str:
    """Load rules file, stripping YAML frontmatter if present."""
    with open(rules_path) as f:
        content = f.read()

    # Strip frontmatter (content between first two --- lines)
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].lstrip("\n")

    return content


# ---------------------------------------------------------------------------
# Scope note
# ---------------------------------------------------------------------------

def build_scope_note(meta: dict, skipped_chars: int) -> str:
    """Build the SCOPE_NOTE block with PR-specific stats."""
    return f"""\
## What you are NOT seeing (and should not flag)

These file types were stripped from the diff to save tokens:
- src/htan_*/datamodel/*.py   (generated Python dataclasses)
- JSON_Schemas/*.json          (generated Synapse JSON schemas)

You are reviewing ONLY source YAML changes. Do not audit unchanged schema content.

Modules in this repo:
Biospecimen | Clinical | CoreFile | DigitalPathology | Imaging | \
MultiplexMicroscopy | scRNA-seq | Sequencing | SpatialOmics | WES

Changed files: {meta['changedFiles']} files, \
+{meta['additions']}/-{meta['deletions']} lines
({skipped_chars:,} chars of generated files removed from diff)"""


# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

def build_reviewer_prompt(
    persona: str,
    checks: str,
    diff: str,
    full_files: str,
    meta: dict,
    rules: str,
    skipped_chars: int,
) -> str:
    """Build prompt for a specialized reviewer agent."""
    scope_note = build_scope_note(meta, skipped_chars)
    full_files_section = ""
    if full_files:
        full_files_section = f"""
---

## Full Content of Changed YAML Files

Use these to verify context around changes (inheritance, enum ordering, slot
completeness). Do NOT audit content that was not changed in the diff.

{full_files}
"""

    return f"""\
{persona}

{CHANGES_ONLY_CONSTRAINT}

{CANONICAL_EXAMPLES}

---

{rules}

---

{checks}

---

{HARD_CONSTRAINTS}

{REVIEWER_OUTPUT_FORMAT}

---

## PR #{meta['number']} — {meta['title']}

**Description:** {meta.get('body') or '(none)'}

{scope_note}

## Diff (source YAML files only)

{diff}
{full_files_section}"""


def build_structural_prompt(diff: str, full_files: str, meta: dict, rules: str, skipped_chars: int) -> str:
    checks = """\
## Your Checks

Apply to changed slots/classes/enums only:

### Structural (Blocking)
- Inheritance correctness — verify is_a chains, no level skipping
- Inlining of nested objects — range with identifier:true needs inlined/inlined_as_list
- Slot completeness — range, title, description on every slot
- Required/optional intent — required: true is explicit
- Enum integrity — alphabetical order, descriptions, no duplicates
- Generated artifacts — only if PR claims to include them"""
    return build_reviewer_prompt(STRUCTURAL_PERSONA, checks, diff, full_files, meta, rules, skipped_chars)


def build_biological_prompt(diff: str, full_files: str, meta: dict, rules: str, skipped_chars: int) -> str:
    checks = """\
## Your Checks

Apply to changed classes/slots only:

- **Provenance Chain [WARNING]**: new assay-level class without biospecimen anchor
  (must inherit or define a link to HTAN_BIOSPECIMEN_ID via HTAN_PARENT_ID)
- **Wet-Lab Nuance [INFO]**: new assay class in MultiplexMicroscopy, SpatialOmics,
  scRNA-seq, or DigitalPathology without dedicated parameter slots
- **Ontology Alignment [WARNING]**: new disease/anatomy/treatment slots without
  reference to NCIT, UBERON, or MONDO
- **Cardinality Sanity [WARNING]**: `multivalued: true` on logically-singular slots;
  `required: true` newly added on clinical slots routinely absent in practice
- **Enum Exclusivity [WARNING]**: overlapping permissible values within an enum
  (e.g., "Adenocarcinoma" vs "Adenocarcinoma, NOS")"""
    return build_reviewer_prompt(BIOLOGICAL_PERSONA, checks, diff, full_files, meta, rules, skipped_chars)


def build_coverage_prompt(diff: str, full_files: str, meta: dict, rules: str, skipped_chars: int) -> str:
    checks = """\
## Your Checks

Apply to changed content only:

### Coverage (Warning)
- New class: test for existence in sv.all_classes(), is_a, required/optional slots,
  valid/invalid instances
- New required slot: test data updated, slot asserted as required
- New enum: valid/invalid value tests
- New module: tests/test_<module>.py with full coverage

### Dependency (Info)
- LinkML pin >2 minor versions behind stable → note
- Deprecated LinkML API usage → note with upgrade path
- Schema version bump needed for substantial changes → note

### Advanced
- **Identifier Strategy [BLOCKING if violated]**: new `identifier: true` slots MUST
  include a `pattern:` regex matching HTAN identifier format
- **Slot Overloading [WARNING]**: generic names (type, value, status, code, result)
  without module-specific prefix
- **Unit Consistency [WARNING]**: physical-quantity slots lacking unit_of_measurement
  (_DAYS suffix slots exempt)"""
    return build_reviewer_prompt(COVERAGE_PERSONA, checks, diff, full_files, meta, rules, skipped_chars)


def build_synthesis_prompt(
    structural_output: str,
    biological_output: str,
    coverage_output: str,
    meta: dict,
    skipped_chars: int,
) -> str:
    """Build the synthesis prompt from 3 reviewer outputs."""
    scope_note = build_scope_note(meta, skipped_chars)

    return f"""\
{SYNTHESIS_PERSONA}

{CHANGES_ONLY_CONSTRAINT}

---

{OUTPUT_FORMAT}

{TASK_STEPS}

---

## PR #{meta['number']} — {meta['title']}

**Description:** {meta.get('body') or '(none)'}

{scope_note}

---

## Structural Reviewer Output

{structural_output}

---

## Biological Reviewer Output

{biological_output}

---

## Coverage Reviewer Output

{coverage_output}
"""


# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------

def call_claude(prompt: str, model: str, max_tokens: int) -> str:
    """Make a single Claude API call and return the response text."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        raise SystemExit(1)

    payload = json.dumps({
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"API error {e.code}: {e.reason}", file=sys.stderr)
        print(body, file=sys.stderr)
        raise SystemExit(1)

    return result["content"][0]["text"]


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Multi-agent AI review pipeline for HTAN schema PRs"
    )
    parser.add_argument("--diff", required=True, help="Path to PR diff file")
    parser.add_argument("--meta", required=True, help="Path to PR metadata JSON")
    parser.add_argument(
        "--rules", required=True,
        help="Path to review rules (e.g. .claude/skills/review-schema-pr/SKILL.md)"
    )
    parser.add_argument(
        "--full-files", default=None,
        help="Directory containing full YAML files at PR head SHA"
    )
    parser.add_argument("--out", required=True, help="Output path for final review")
    parser.add_argument(
        "--model", default=DEFAULT_MODEL,
        help=f"Claude model to use (default: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Write prompts to /tmp/ without making API calls"
    )
    args = parser.parse_args()

    # Load inputs
    with open(args.diff) as f:
        raw_diff = f.read()
    with open(args.meta) as f:
        meta = json.load(f)

    rules = load_rules(args.rules)
    diff, skipped_chars = filter_diff(raw_diff)
    full_files = load_full_files(args.full_files)

    print(
        f"Diff: {len(diff):,} chars after filtering "
        f"({skipped_chars:,} chars of generated files removed)"
    )
    if full_files:
        print(f"Full files: {len(full_files):,} chars loaded")

    # Build reviewer prompts
    prompts = {
        "structural": build_structural_prompt(diff, full_files, meta, rules, skipped_chars),
        "biological": build_biological_prompt(diff, full_files, meta, rules, skipped_chars),
        "coverage": build_coverage_prompt(diff, full_files, meta, rules, skipped_chars),
    }

    if args.dry_run:
        for name, prompt in prompts.items():
            path = f"/tmp/review_prompt_{name}.txt"
            with open(path, "w") as f:
                f.write(prompt)
            print(f"  {name}: {path} ({len(prompt):,} chars)")

        # Build a placeholder synthesis prompt
        synthesis = build_synthesis_prompt(
            "[dry-run: no structural output]",
            "[dry-run: no biological output]",
            "[dry-run: no coverage output]",
            meta, skipped_chars,
        )
        synth_path = "/tmp/review_prompt_synthesis.txt"
        with open(synth_path, "w") as f:
            f.write(synthesis)
        print(f"  synthesis: {synth_path} ({len(synthesis):,} chars)")
        print("Dry run complete — no API calls made.")
        return

    # Phase 1: Run 3 reviewers in parallel
    print(f"Running 3 reviewers in parallel (model: {args.model})...")
    outputs: dict[str, str] = {}

    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {
            pool.submit(call_claude, prompt, args.model, REVIEWER_MAX_TOKENS): name
            for name, prompt in prompts.items()
        }
        for future in as_completed(futures):
            name = futures[future]
            outputs[name] = future.result()
            print(f"  {name}: {len(outputs[name]):,} chars")

    # Phase 2: Synthesis
    print("Running synthesis...")
    synthesis_prompt = build_synthesis_prompt(
        outputs["structural"],
        outputs["biological"],
        outputs["coverage"],
        meta, skipped_chars,
    )

    review = call_claude(synthesis_prompt, args.model, SYNTHESIS_MAX_TOKENS)
    print(f"  synthesis: {len(review):,} chars")

    # Write output
    with open(args.out, "w") as f:
        f.write(review)

    print(f"Review written to {args.out}")


if __name__ == "__main__":
    main()
