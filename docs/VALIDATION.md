# Validation status

Last checked: 2026-10-03 with KiCad CLI 10.0.6 on the files in the initial archive.

## Baseline results

| Check | Result | Meaning |
|---|---:|---|
| Repository integrity script | Pass | Expected files and basic metadata are present and internally consistent at the packaging level |
| Schematic ERC | 15 errors, 40 warnings | The legacy conceptual schematic is not electrically clean |
| PCB DRC | 408 violations | The layout contains shorts, clearances, crossings, mask, and other rule failures |
| PCB unrouted items | 126 | Routing is incomplete |
| BOM-to-PCB reference check | R1 absent from PCB | The current-shunt BOM item is not represented by a PCB footprint and must be reconciled |
| Bench test | Not performed | No electrical, thermal, RF, or functional behavior has been demonstrated |

The counts above are a baseline, not a waiver. Full machine-generated reports are intentionally not committed because paths, locale, and KiCad versions affect their formatting. Generate fresh reports from the exact revision under review.

## Reproduce the checks

From the repository root, first run the packaging validation:

```bash
python3 scripts/validate_repo.py
```

Then run KiCad's electrical and board checks:

```bash
kicad-cli sch erc --exit-code-violations \
  -o erc-report.txt hardware/Nylok_Heater.sch

kicad-cli pcb drc --exit-code-violations \
  -o drc-report.txt hardware/Nylok_Heater.kicad_pcb
```

The KiCad commands are expected to exit nonzero at the initial concept revision because they detect violations.

## Fabrication blockers

Before fabrication, at minimum:

1. Convert and fully repair the schematic in the current KiCad format.
2. Verify every symbol pin number, footprint, polarity, and manufacturer part number against primary datasheets.
3. Reconcile the schematic, BOM, logical net map, and PCB netlist.
4. Complete routing and obtain clean ERC and DRC reports with reviewed rule settings.
5. Recalculate high-current paths, copper weight, connector ratings, MOSFET losses, shunt/Kelvin layout, regulator compensation, thermal relief, and thermal vias.
6. Validate the external ZVS driver, tank capacitor, coil, loaded impedance, resonant current/voltage, EMI, and control method as one system.
7. Add and review battery protection, fusing, undervoltage behavior, fault shutdown, watchdog, enclosure, guarding, and thermal cutoffs.
8. Perform staged bench testing from a current-limited isolated supply, followed by instrumented thermal and fault testing.
9. Record objective evidence and obtain an independent engineering review before changing the repository status.

No Gerbers, drill files, pick-and-place data, assembly drawings, or fabrication release are provided while these blockers remain.
