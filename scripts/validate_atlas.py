#!/usr/bin/env python3
"""Check schema, identifiers, controls, site data sync and Kinbank control integrity."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "data" / "atlas.csv"
MIRROR = ROOT / "docs" / "assets" / "atlas.csv"
CTRL = ROOT / "data" / "kinbank_vnv_control.csv"
CTRL_MIRROR = ROOT / "docs" / "assets" / "kinbank_vnv_control.csv"
REQUIRED = {
    "id", "form", "language", "region", "recorded_association", "ipa", "source_url",
    "verification_status", "original_script", "language_family", "variety",
    "earliest_witness", "lexical_meaning", "sacred_role", "access_code",
    "record_type", "relationship_group", "control_flag", "ipa_confidence",
    "etymology_status", "retrieval_tags", "open_questions"
}

def fail(msg):
    raise SystemExit(f"VALIDATION FAILURE: {msg}")

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as h:
        reader = csv.DictReader(h)
        if not reader.fieldnames:
            fail(f"{path} missing header")
        result = list(reader)
    return reader.fieldnames, result

fields, rows = read_csv(MAIN)
missing = REQUIRED - set(fields)
if missing:
    fail(f"missing columns: {sorted(missing)}")
if len(fields) != len(set(fields)):
    fail("duplicate columns")
if len(rows) != 83:
    fail(f"expected 83 Pass-03 index rows, found {len(rows)}; update test intentionally for later imports")
ids = [r["id"] for r in rows]
if len(ids) != len(set(ids)):
    fail("duplicate record ID")
for r in rows:
    if not r["form"] or not r["language"]:
        fail(f"missing identity for {r['id']}")
    if r["access_code"] not in {"DOC", "COL", "NAR", "VAR", ""}:
        fail(f"unknown access code at {r['id']}")
    if r["control_flag"] not in {"true", "false"}:
        fail(f"invalid control flag at {r['id']}")
    if r["ipa"] and r["ipa_confidence"] in {"", "unavailable"}:
        fail(f"IPA confidence missing at {r['id']}")
if MAIN.read_bytes() != MIRROR.read_bytes():
    fail("published Pages atlas copy is not identical to data/atlas.csv")
if CTRL.read_bytes() != CTRL_MIRROR.read_bytes():
    fail("published Pages control copy is not identical to data/kinbank_vnv_control.csv")
_, controls = read_csv(CTRL)
if len(controls) != 18:
    fail("control table must have 18 trigrams")
print(f"PASS: {len(rows)} indexed names, {len(controls)} VNV controls, synced Pages assets")
