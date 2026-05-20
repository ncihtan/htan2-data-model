#!/usr/bin/env python3
"""
Rebuild modules/Biospecimen/domains/icdo3_morphology_enum.yaml from the
NAACCR ICD-O-3 Histology table. End-to-end: downloads Histology3 v26 from
naaccr.org, parses it, and writes the YAML.

The previous extraction produced an enum with only 184 codes, all from the
9xxx hematologic block — the entire 8xxx solid-tumor block (carcinomas,
sarcomas, melanomas, epithelial tumors) was missing, including 8140/3
"Adenocarcinoma, NOS" (issue #185).

Source (NAACCR Histology v26, released 2025-09-03):
    https://www.naaccr.org/icdo3/
        Histology3_v26_20250903.xlsx

Sheet "Histology3" has 4 columns:
    Value (4-digit morphology, e.g. "8140")
    strHistologyBehaviour (single digit: 0,1,2,3,6,9)
    Preferred (True for the canonical label, False for synonyms)
    label (text description)

Each code (Value + "/" + Behaviour) has exactly one Preferred=True row. We
emit one permissible value per unique code using its preferred label.

Usage:
    # End-to-end: fetch xlsx, build YAML
    python3 scripts/build_icdo3_enum.py

    # Or point at a locally-cached xlsx
    python3 scripts/build_icdo3_enum.py --histology-xlsx /path/to/Histology3_v26_20250903.xlsx

Pass `--behaviors 2,3` to filter to malignant + in-situ codes only.
"""
import argparse
import io
import urllib.request
from pathlib import Path

import openpyxl

NAACCR_XLSX_URL = (
    "https://www.naaccr.org/wp-content/uploads/2025/09/Histology3_v26_20250903.xlsx"
)

HEADER = """\
name: IcdO3MorphologyEnum
id: https://w3id.org/htan/icdo3_morphology_enum
description: ICD-O-3 morphology codes sourced from the NAACCR Histology table ({version})

prefixes:
  htan: https://w3id.org/htan/
  linkml: https://w3id.org/linkml/
  NCIT: http://purl.obolibrary.org/obo/NCIT_

default_prefix: htan

enums:
  IcdO3MorphologyEnum:
    title: icdo3_morphology
    permissible_values:
"""


def escape_yaml_double_quoted(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def fetch_workbook_bytes() -> bytes:
    """Download the NAACCR Histology3 v26 xlsx and return its bytes."""
    print(f"Downloading {NAACCR_XLSX_URL}")
    req = urllib.request.Request(
        NAACCR_XLSX_URL,
        headers={"User-Agent": "htan2-data-model-build-icdo3-enum/1.0"},
    )
    with urllib.request.urlopen(req) as resp:
        return resp.read()


def parse_histology(source, behaviors: set[str] | None):
    """Yield (code, label) for each preferred row, optionally filtered by behavior.

    `source` may be a Path to a local xlsx or a bytes/BytesIO of one.
    """
    if isinstance(source, (bytes, bytearray)):
        source = io.BytesIO(source)
    wb = openpyxl.load_workbook(
        source if not isinstance(source, Path) else str(source),
        read_only=True,
        data_only=True,
    )
    ws = wb["Histology3"]
    seen: dict[str, str] = {}
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i == 0:
            continue
        value, behaviour, preferred, label = row[:4]
        if value is None or behaviour is None or preferred is not True:
            continue
        behaviour = str(behaviour).strip()
        if behaviors and behaviour not in behaviors:
            continue
        code = f"{str(value).strip()}/{behaviour}"
        if not label:
            continue
        seen[code] = str(label).strip()
    wb.close()
    return seen


def write_enum(rows: dict[str, str], output: Path, version: str) -> int:
    pairs = sorted(rows.items(), key=lambda kv: kv[0])
    with output.open("w", encoding="utf-8") as fh:
        fh.write(HEADER.format(version=version))
        for code, label in pairs:
            fh.write(f'      "{code}":\n')
            fh.write(
                f'        description: "{escape_yaml_double_quoted(label)}"\n'
            )
    return len(pairs)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument(
        "--histology-xlsx",
        type=Path,
        help="Path to a locally-cached Histology3 xlsx. "
        "If omitted, NAACCR v26 is downloaded.",
    )
    ap.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent
        / "modules/Biospecimen/domains/icdo3_morphology_enum.yaml",
    )
    ap.add_argument(
        "--version",
        default="Histology3 v26, 2025-09-03",
        help="NAACCR Histology release identifier for the header description",
    )
    ap.add_argument(
        "--behaviors",
        help="Comma-separated behavior digits to keep (e.g. '2,3'). Default: all.",
    )
    args = ap.parse_args()

    behaviors = (
        {b.strip() for b in args.behaviors.split(",")} if args.behaviors else None
    )
    source = args.histology_xlsx if args.histology_xlsx else fetch_workbook_bytes()
    rows = parse_histology(source, behaviors)
    n = write_enum(rows, args.output, args.version)
    print(f"Wrote {n} permissible values to {args.output}")


if __name__ == "__main__":
    main()
