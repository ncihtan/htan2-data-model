#!/usr/bin/env python3
"""
Rebuild modules/Biospecimen/domains/icd10_disease_enum.yaml from the CDC
ICD-10-CM "order" flat file. End-to-end: downloads the FY2026 zip from
the CDC FTP, extracts the order file, parses it, and writes the YAML.

The previous extraction parsed the *alphabetical index* XML and produced an
enum with only ~20k codes and lay-term descriptions (e.g. "Eberth's disease"
for A01.00). It is missing codes that are not cross-referenced by keyword in
the index — notably C77.* and several C78.* including C78.7 (issue #185).

Source (FY2026 release, effective 2025-10-01):
    https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2026/
        icd10cm-Code Descriptions-2026.zip  →  icd10cm-order-2026.txt

The order file is fixed-width and lists every ICD-10-CM code (header +
billable), 98,186 rows total. Field layout:
    cols  1- 5  order number
    cols  7-13  code (no decimal, right-padded with spaces)
    col  15     billable flag (0 = header / non-billable, 1 = billable)
    cols 17-76  short description (60 chars)
    cols 78-..  long description

Decimal restoration follows ICD-10-CM convention: codes ≤ 3 chars are
category headers (no decimal); codes ≥ 4 chars get a decimal after the
3rd character (`C787` → `C78.7`, `C7800` → `C78.00`).

Usage:
    # End-to-end: fetch CDC zip, extract, build YAML
    python3 scripts/build_icd10_enum.py

    # Or point at a locally-cached order file
    python3 scripts/build_icd10_enum.py --order-file /path/to/icd10cm-order-2026.txt

Pass `--billable-only` to exclude the ~23k non-billable header rows.
"""
import argparse
import io
import urllib.request
import zipfile
from pathlib import Path

CDC_ZIP_URL = (
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/"
    "2026/icd10cm-Code%20Descriptions-2026.zip"
)
ORDER_FILE_IN_ZIP = "icd10cm-order-2026.txt"

HEADER = """\
name: Icd10DiseaseEnum
id: https://w3id.org/htan/icd10_disease_enum
description: ICD-10-CM disease codes (FY{year} release) sourced from the CDC ICD-10-CM order file

prefixes:
  htan: https://w3id.org/htan/
  linkml: https://w3id.org/linkml/
  NCIT: http://purl.obolibrary.org/obo/NCIT_

default_prefix: htan

enums:
  Icd10DiseaseEnum:
    title: icd10_disease_code
    permissible_values:
"""


def format_code(code: str) -> str:
    """Insert the ICD-10-CM decimal after the 3rd character if present."""
    code = code.strip()
    if len(code) <= 3:
        return code
    return f"{code[:3]}.{code[3:]}"


def escape_yaml_double_quoted(s: str) -> str:
    """Escape a string for use inside a YAML double-quoted scalar."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def parse_order_text(text: str, billable_only: bool):
    """Yield (formatted_code, long_description) for each row."""
    for line in text.splitlines():
        if len(line) < 78:
            continue
        code = line[6:13].strip()
        billable = line[14] == "1"
        long_desc = line[77:].strip()
        if billable_only and not billable:
            continue
        if not code or not long_desc:
            continue
        yield format_code(code), long_desc


def fetch_order_text() -> str:
    """Download the CDC FY2026 zip and return the order file contents."""
    print(f"Downloading {CDC_ZIP_URL}")
    with urllib.request.urlopen(CDC_ZIP_URL) as resp:
        data = resp.read()
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        return zf.read(ORDER_FILE_IN_ZIP).decode("utf-8")


def write_enum(rows, output: Path, year: str) -> int:
    pairs = sorted(set(rows), key=lambda kv: kv[0])
    with output.open("w", encoding="utf-8") as fh:
        fh.write(HEADER.format(year=year))
        for code, desc in pairs:
            fh.write(f'      "{code}":\n')
            fh.write(f'        description: "{escape_yaml_double_quoted(desc)}"\n')
    return len(pairs)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument(
        "--order-file",
        type=Path,
        help="Path to a locally-cached icd10cm-order-YYYY.txt. "
        "If omitted, the FY2026 zip is downloaded from the CDC.",
    )
    ap.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent
        / "modules/Biospecimen/domains/icd10_disease_enum.yaml",
    )
    ap.add_argument(
        "--year",
        default="2026",
        help="ICD-10-CM release year for the header description",
    )
    ap.add_argument(
        "--billable-only",
        action="store_true",
        help="Exclude non-billable category headers (~23k rows)",
    )
    args = ap.parse_args()

    if args.order_file:
        text = args.order_file.read_text(encoding="utf-8")
    else:
        text = fetch_order_text()

    rows = list(parse_order_text(text, args.billable_only))
    n = write_enum(rows, args.output, args.year)
    print(f"Wrote {n} permissible values to {args.output}")


if __name__ == "__main__":
    main()
