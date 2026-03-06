# HTAN Data Model — AI Review Guidelines

This file governs how Claude Code reviews pull requests in this repository.
**Only flag issues in the categories below. Do not comment on general Python style,
prose quality, or anything outside this scope.**

---

## Repo Conventions (Required Reading)

- Slot names: `ALL_CAPS_WITH_UNDERSCORES`
- Enum names: `CamelCase`
- Titles: `Title Case`
- Descriptions: sentence case, first word capitalised
- All enum permissible values: alphabetically ordered
- Every slot must have `title` and `description`
- Generated artifacts (`src/*/datamodel/*.py`, `JSON_Schemas/*.json`) are produced
  in a separate downstream PR — do not require them in the same PR as YAML changes

---

## Review Checklist

### 🔴 Structural — flag as blocking

These must be resolved before merge.

#### Inheritance correctness
- Every `BulkWESLevel<N>` must inherit `BaseSequencingLevel<N>Attributes`
- Every `scRNALevel<N>` must inherit `BaseSequencingLevel<N>Attributes`
- `BaseSequencingLevel1Attributes` is_a `BaseSequencingAttributes`
- `BaseSequencingLevel2Attributes` is_a `BaseSequencingLevel1Attributes`
- `BaseSequencingLevel3Attributes` is_a `BaseSequencingLevel2Attributes`
- No level class may skip a level (e.g. Level3 directly is_a BaseSequencingAttributes)
- New assay modules must follow the same level hierarchy pattern

#### Inlining of nested objects
- Any slot whose `range` is a class that contains `identifier: true` MUST have
  either `inlined: true` (single value) or `inlined_as_list: true` (multivalued)
- Missing `inlined` causes the loader to silently coerce the nested object to a
  string identifier, breaking nested field validation

#### Slot completeness
- Every slot must have: `range`, `title`, `description`
- Required slots must be explicitly marked `required: true`
- Optional slots must not be implicitly required through inheritance without intent

#### Enum integrity
- Permissible values must be alphabetically ordered within each enum
- Every permissible value must have a `description`
- No duplicate permissible values within an enum

#### Generated artifacts
- Generated artifacts (`src/*/datamodel/*.py`, `JSON_Schemas/*.json`) are intentionally
  produced in a **separate downstream PR** via `make gen-schema`. Do NOT flag their
  absence in a PR that only modifies `domains/*.yaml` files.
- Only flag as blocking if a PR explicitly claims to include regenerated artifacts
  but the diff shows they are missing or stale.

---

### 🟡 Coverage — flag as warning

Flag if missing, but do not block merge. Note which tests are absent.

#### New class added
- Test asserts the class exists in `sv.all_classes()`
- Test asserts correct `is_a` value
- Test asserts all required slots are present and marked required
- Test asserts optional slots are not required
- At least one valid instance loads without error
- At least one invalid instance (missing required field or bad enum value) raises `ValueError`

#### New required slot added to existing class
- Valid test data files updated to include the new slot
- Test asserts the slot is required

#### New enum added
- Test asserts an invalid value raises an error
- Test asserts a valid value loads correctly

#### New module added
- `tests/test_<module>.py` exists
- Tests cover: schema loading, class structure, inheritance, enums, valid data, invalid data

---

### 🔵 Dependency — flag as informational

Note in review, no action required from author.

#### LinkML version
- If `pyproject.toml` shows a LinkML pin more than 2 minor versions behind the
  current stable release, note it
- If the diff introduces usage of deprecated LinkML APIs (e.g.
  `dataclass_extensions_376`, `dataclasses_init_fn_with_kwargs`), note the
  deprecation warning and link to the LinkML upgrade path

#### Schema version
- If domain YAML changes are substantial (new classes, restructured hierarchy),
  note whether `version:` in the schema header should be bumped

---

## What NOT to Flag

Do not comment on:
- Python code style, formatting, or naming outside of schema-generated files
- Prose in README, CONTRIBUTING.md, or docs
- General test verbosity or structure, as long as coverage rules above are met
- YAML indentation if it is consistent with the file's existing style
- Ordering of slots within a class (only enum values must be alphabetical)
- Anything in `archive/`

---

## Severity Labels to Use in Review Comments

| Label | Meaning |
|---|---|
| `[BLOCKING]` | Must be fixed before merge |
| `[WARNING]` | Should be addressed; author should explain if skipping |
| `[INFO]` | Noted for awareness, no action required |

Use exactly these labels at the start of each comment. Do not invent others.
