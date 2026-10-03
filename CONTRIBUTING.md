# Contributing

Thank you for helping improve the Nylok heater controller concept.

## Before proposing a change

1. Read the safety and design warnings in the main README.
2. Open an issue for material electrical, thermal, mechanical, or architecture changes.
3. Base component choices on manufacturer documentation and identify the exact part/package revision.
4. Keep estimates, simulations, and measured results clearly distinguished.

## Pull-request checklist

- Run `python3 scripts/validate_repo.py`.
- Open the project in KiCad 10 or later.
- Run ERC and DRC; attach the reports or summarize every changed violation count.
- Update the BOM and net map when affected.
- Include measurement conditions, equipment, units, uncertainty, and raw evidence for bench-tested claims.
- Update the README and changelog when maturity or safety status changes.
- Do not commit generated cache, lock, backup, or fabrication-output files.

Small, focused pull requests are easiest to review. Changes that could cause battery, thermal, RF, or high-current hazards require an independent engineering review before merge.
