"""Tests for scripts/build_uberon_enum.py using a small offline OBO fixture."""

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import build_uberon_enum as b  # noqa: E402

SCRIPT = Path(__file__).parent.parent / "scripts/build_uberon_enum.py"

OBO = """\
format-version: 1.2
data-version: uberon/releases/2026-10-01/uberon-basic.owl

[Term]
id: UBERON:0000001
name: anatomical structure

[Term]
id: UBERON:0000310
name: breast
is_a: UBERON:0000001 ! anatomical structure

[Term]
id: UBERON:0000000
name: obsolete processual entity
is_obsolete: true

[Term]
id: UBERON:0000099
name: old breast term
is_obsolete: true
replaced_by: UBERON:0000310

[Term]
id: UBERON:0000022
name: feather
is_a: UBERON:0000001 ! anatomical structure
relationship: never_in_taxon NCBITaxon:314146

[Term]
id: UBERON:0008291
name: down feather
is_a: UBERON:0000022 ! feather

[Term]
id: UBERON:0008294
name: feather barb
relationship: part_of UBERON:0000022 ! feather

[Term]
id: UBERON:0000151
name: pectoral fin
relationship: never_in_taxon NCBITaxon:32523

[Term]
id: UBERON:0003101
name: male organism
relationship: never_in_taxon NCBITaxon:10090

[Typedef]
id: part_of
name: part of
"""


def test_select_terms_drops_obsolete_and_non_human():
    codes = b.select_terms(b.parse_terms(OBO), keep_non_human=False)
    assert set(codes) == {"UBERON:0000001", "UBERON:0000310", "UBERON:0003101"}
    assert codes["UBERON:0000310"] == "breast"


def test_non_human_exclusion_propagates_via_is_a_and_part_of():
    excluded = b.non_human_terms(b.parse_terms(OBO))
    assert {"UBERON:0000022", "UBERON:0008291", "UBERON:0008294"} <= excluded
    # never_in mouse only does not exclude a term from the human enum
    assert "UBERON:0003101" not in excluded


def test_keep_non_human_retains_taxon_restricted_terms():
    codes = b.select_terms(b.parse_terms(OBO), keep_non_human=True)
    assert "UBERON:0000022" in codes
    assert "UBERON:0000000" not in codes


def test_script_writes_valid_enum_yaml_with_release(tmp_path):
    obo = tmp_path / "uberon-basic.obo"
    obo.write_text(OBO)
    out = tmp_path / "uberon_tissues.yaml"
    subprocess.run(
        [sys.executable, str(SCRIPT), "--obo-file", str(obo), "--output", str(out)],
        check=True,
    )
    schema = yaml.safe_load(out.read_text())
    assert schema["version"] == "2026-10-01"
    assert "v2026-10-01" in schema["source"]
    pvs = schema["enums"]["tissue_or_organ_of_origin_uberon_enum"]["permissible_values"]
    assert list(pvs) == sorted(pvs)
    assert pvs["UBERON:0000310"]["description"] == "breast"
    assert b.existing_codes(out) == set(pvs)


def test_release_tag_overrides_obo_data_version(tmp_path):
    # GitHub tag v2026-06-23 ships data-version 2026-06-19; the tag wins.
    obo = tmp_path / "uberon-basic.obo"
    obo.write_text(OBO)
    out = tmp_path / "out.yaml"
    subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--obo-file",
            str(obo),
            "--release",
            "2026-06-23",
            "--output",
            str(out),
        ],
        check=True,
    )
    assert yaml.safe_load(out.read_text())["version"] == "2026-06-23"


def test_if_missing_leaves_existing_file_untouched(tmp_path):
    out = tmp_path / "uberon_tissues.yaml"
    out.write_text("sentinel\n")
    subprocess.run(
        [sys.executable, str(SCRIPT), "--if-missing", "--output", str(out)], check=True
    )
    assert out.read_text() == "sentinel\n"


def test_diff_codes_reports_added_and_removal_reasons():
    terms = b.parse_terms(OBO)
    new = b.select_terms(terms, keep_non_human=False)
    old = {"UBERON:0000001", "UBERON:0000099", "UBERON:0000022", "UBERON:9999999"}
    added, removed = b.diff_codes(old, new, terms)
    assert added == ["UBERON:0000310", "UBERON:0003101"]
    assert removed == [
        ("UBERON:0000022", "feather", "never in Homo sapiens"),
        ("UBERON:0000099", "old breast term", "obsolete -> UBERON:0000310"),
        ("UBERON:9999999", "", "not in this release"),
    ]


def test_diff_codes_obsolete_without_replacement():
    terms = b.parse_terms(OBO)
    _, removed = b.diff_codes({"UBERON:0000000"}, {}, terms)
    assert removed == [("UBERON:0000000", "obsolete processual entity", "obsolete")]


class _FakeResponse:
    def __init__(self, url: str):
        self._url = url

    def geturl(self) -> str:
        return self._url

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def test_resolve_latest_release_follows_redirect(monkeypatch):
    url = "https://github.com/obophenotype/uberon/releases/tag/v2026-10-01"
    monkeypatch.setattr(b, "_open", lambda _url: _FakeResponse(url))
    assert b.resolve_latest_release() == "2026-10-01"


def test_resolve_latest_release_rejects_unexpected_url(monkeypatch):
    url = "https://github.com/obophenotype/uberon/releases"
    monkeypatch.setattr(b, "_open", lambda _url: _FakeResponse(url))
    with pytest.raises(SystemExit):
        b.resolve_latest_release()


def test_existing_codes_missing_file_is_empty(tmp_path):
    assert b.existing_codes(tmp_path / "missing.yaml") == set()


def test_load_obo_uses_data_version_for_local_file(tmp_path):
    obo = tmp_path / "uberon-basic.obo"
    obo.write_text(OBO)
    text, release = b._load_obo(None, obo)
    assert release == "2026-10-01"
    assert text == OBO


def test_load_obo_downloads_latest_when_no_release(monkeypatch):
    monkeypatch.setattr(b, "resolve_latest_release", lambda: "2026-10-01")
    monkeypatch.setattr(b, "fetch_obo_text", lambda release: OBO)
    assert b._load_obo(None, None) == (OBO, "2026-10-01")


def test_load_obo_rejects_file_without_data_version(tmp_path):
    obo = tmp_path / "uberon-basic.obo"
    obo.write_text("format-version: 1.2\n")
    with pytest.raises(SystemExit):
        b._load_obo("2026-10-01", obo)
