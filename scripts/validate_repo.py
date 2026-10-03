#!/usr/bin/env python3
"""Validate the repository package without claiming electrical correctness."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWN_MISSING_PCB_REFS = {"R1"}
REQUIRED = (
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "hardware/Nylok_Heater.kicad_pro",
    "hardware/Nylok_Heater.kicad_pcb",
    "hardware/Nylok_Heater.sch",
    "hardware/BOM.csv",
    "hardware/NETS.csv",
    "docs/Induction_System_Specification.md",
    "docs/Nylok_Labeled_PCB_and_Connections.png",
    "docs/VALIDATION.md",
    "fab/FABRICATION_NOTES.md",
    "renders/PCB_Perspective_Render.png",
    "renders/PCB_Top_View.png",
)


def read_csv(relative_path: str) -> tuple[list[str], list[dict[str, str]]]:
    with (ROOT / relative_path).open(newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        return list(reader.fieldnames or []), list(reader)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for relative_path in REQUIRED:
        path = ROOT / relative_path
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty required file: {relative_path}")

    try:
        project = json.loads((ROOT / "hardware/Nylok_Heater.kicad_pro").read_text())
        if project.get("meta", {}).get("filename") != "Nylok_Heater.kicad_pro":
            errors.append("KiCad project metadata filename is unexpected")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid KiCad project JSON: {exc}")

    bom_header, bom_rows = read_csv("hardware/BOM.csv")
    expected_bom_header = ["Reference", "Symbol/MPN", "Value", "Footprint", "Function"]
    if bom_header != expected_bom_header:
        errors.append(f"unexpected BOM header: {bom_header}")
    bom_refs = [row.get("Reference", "").strip() for row in bom_rows]
    if not bom_refs or any(not ref for ref in bom_refs):
        errors.append("BOM contains a blank reference or no rows")
    if len(bom_refs) != len(set(bom_refs)):
        errors.append("BOM contains duplicate references")

    nets_header, nets_rows = read_csv("hardware/NETS.csv")
    if nets_header != ["Net", "Connections"]:
        errors.append(f"unexpected net-map header: {nets_header}")
    csv_nets = {row.get("Net", "").strip() for row in nets_rows}
    if "GND" not in csv_nets:
        errors.append("logical net map does not contain GND")

    pcb_path = ROOT / "hardware/Nylok_Heater.kicad_pcb"
    pcb_text = pcb_path.read_text(encoding="utf-8")
    if not pcb_text.startswith("(kicad_pcb "):
        errors.append("PCB file does not have a KiCad PCB header")
    pcb_refs = set(re.findall(r'^\s*\(property "Reference" "([^\"]+)"', pcb_text, re.M))
    missing_refs = set(bom_refs) - pcb_refs
    unexpected_missing_refs = sorted(missing_refs - KNOWN_MISSING_PCB_REFS)
    if unexpected_missing_refs:
        errors.append(
            "new BOM references absent from PCB: " + ", ".join(unexpected_missing_refs)
        )
    known_missing_refs = sorted(missing_refs & KNOWN_MISSING_PCB_REFS)
    if known_missing_refs:
        warnings.append(
            "known design blocker—BOM references absent from PCB: "
            + ", ".join(known_missing_refs)
        )
    pcb_nets = set(re.findall(r'^\s*\(net \d+ "([^\"]+)"\)', pcb_text, re.M))
    missing_nets = sorted(csv_nets - pcb_nets)
    if missing_nets:
        errors.append("logical nets absent from PCB: " + ", ".join(missing_nets))

    schematic = (ROOT / "hardware/Nylok_Heater.sch").read_text(encoding="utf-8")
    if not schematic.startswith("EESchema Schematic File Version") or "$EndSCHEMATC" not in schematic:
        errors.append("legacy schematic framing is invalid")

    for relative_path in (
        "docs/Nylok_Labeled_PCB_and_Connections.png",
        "renders/PCB_Perspective_Render.png",
        "renders/PCB_Top_View.png",
    ):
        if (ROOT / relative_path).read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append(f"invalid PNG signature: {relative_path}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "do not fabricate or energize" not in readme.lower():
        errors.append("README is missing the fabrication/energizing warning")

    if errors:
        print("Repository validation FAILED:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    for warning in warnings:
        print(f"WARNING: {warning}")

    print(
        "Repository validation passed: "
        f"{len(bom_rows)} BOM rows, {len(nets_rows)} logical nets, "
        f"{len(pcb_refs)} PCB references."
    )
    print("Note: this does not run or replace KiCad ERC/DRC.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
