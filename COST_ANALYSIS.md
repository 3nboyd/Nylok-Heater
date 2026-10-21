# Nylok Handheld Induction Heater — Full Cost Analysis

Full text and tables from the supplied analysis. [Download the original document](Nylok_Heater_Cost_Analysis.docx) or [view the source on Google Drive](https://docs.google.com/document/d/1d1SXaH8sqosNrCxIEX-nSozUCm1gSHQc/edit).

Source pricing was checked October 3, 2026. Costs and performance figures retain the original document’s assumptions, estimates, and exclusions.

Nylok Handheld Induction Heater<br>Breakdown, Calculations,<br>& Cost Analysis

[PCB Board Github](https://github.com/3nboyd/Nylok-Heater)<br>

## NYLOK HANDHELD HEATER / 01 / DECISION

### Best-case performance and build budget

Recommended development platform: two EVE 25P 18650 cells in series, an induction board, and a later custom controller PCB. Proposed battery power targets are 20 W for liquid and 50 W for powder. The selected cells provide current headroom for both modes. The analysis combines component ratings, a localized thermal model, and procurement pricing. (References 1-3, 7)

| Decision | Result |
| --- | --- |
| Basic manually operated heating test assembly | $18.06 estimated parts allocation, before shipping and tax |
| Two-mode controller plus countdown display | $31.37 estimated parts allocation, before shipping and tax |
| Basic heater, 5,000-unit order | $13.14 estimated manufacturing cost per heater, including housing and assembly |
| Two-mode heater, 5,000-unit order | $19.14 estimated manufacturing cost per heater, including housing and assembly |
| Favorable modeled 4 mm steel screw | Liquid: 1.7 s at 20 W; powder: 5.8 s at 50 W |
| Evidence level | Engineering calculations and manufacturer/supplier references; bulk purchasing estimates are identified |

### What "best case" means

The best-case analysis combines an ideal energy floor with a favorable thermal scenario that accounts for axial conduction, convection and radiation. Heating figures are model estimates. The favorable scenario assumes 60% overall battery-to-metal efficiency, a centrally heated 3 mm band on a 60 mm steel shaft, no head or conductive clamp, and room-temperature starting conditions.

### Temperature targets used in the calculations

Liquid target: 65°C / 149°F. Powder target: 232°C / 450°F. These come from the project discussion, not a coating datasheet. The liquid target represents the low end of the stated 150-200°F range. Different chemistry, higher liquid temperature, or required dwell time changes the calculation.

### Two prototype price points and budget boundary

Price point 1: $18.06 for a basic manually operated heating prototype. Price point 2: $31.37 for the proposed heater with regulated two-mode control and an automatic countdown display. The $13.31 difference covers the controller, power regulation, sensing and display. Prototype costs exclude the CAD housing, measuring equipment, programmer, soldering tools, shipping and tax. Listed prices and estimated accessory allocations are separated in the parts list; shipping and small-part minimum-order quantities can increase checkout cost.


## NYLOK HANDHELD HEATER / 02 / PHYSICS

### Localized heating calculations

### Band geometry and ideal energy floor

Approximate the shaft as a solid steel cylinder. Let d be diameter and w = 3 mm be band width. Assumed steel density is 7,850 kg/m³ and heat capacity is 500 J/(kg·K). Thread valleys are omitted. The cylinder approximation slightly overstates band mass for a threaded shaft of the same outside diameter.

Band mass: m = density x pi x d² x w / 4

Coating surface area: A = pi x d x w

Ideal band energy: Q = m x c x (target temperature - 25°C)

| Diameter | Band mass | Area | Liquid Q | Powder Q |
| --- | --- | --- | --- | --- |
| 4 mm | 0.296 g | 37.7 mm² | 5.92 J | 30.63 J |
| 8 mm | 1.184 g | 75.4 mm² | 23.68 J | 122.52 J |

Ideal floor: t = Q / P, assuming 100% efficiency and no heat spreading

| Diameter | Liquid at 20 W | Powder at 50 W |
| --- | --- | --- |
| 4 mm | 0.30 s | 0.61 s |
| 8 mm | 1.18 s | 2.45 s |

The ideal floor and conduction model answer different questions. They assume an isolated band that a real screw does not have. They describe the energy needed for the band volume only, not the full surface-temperature transient.

### Favorable scenario that includes heat spreading

| Diameter | Liquid: 20 W / 65°C | Powder: 50 W / 232°C |
| --- | --- | --- |
| 4 mm, 60% efficiency | 1.7 s | 5.8 s |
| 8 mm, 60% efficiency | 19.1 s | 67.0 s |
| 4 mm, 40% efficiency sensitivity | 3.3 s | 12.3 s |
| 8 mm, 40% efficiency sensitivity | 39.6 s | 124.6 s |

Method: one-dimensional finite-volume conduction with uniform power deposited only within the 3 mm band. k = 45 W/(m·K), convection h = 25 W/(m²·K), emissivity = 0.3, ambient = 25°C, insulated shaft ends. Axial cells are 0.25 mm and time steps 0.01 s. Stop when the coolest modeled band cell reaches the target. At 60% efficiency, metal heating powers are 12 W and 30 W.

The model assumes each cross-section is radially uniform, omits a head and holder heat sink, and assumes the field deposits power in the chosen band. Real coil width, field fringing, alloy and radial gradients can change the result. A long screw can draw more heat into its shaft. These figures apply to the modeled geometry only.


## NYLOK HANDHELD HEATER / 03 / ELECTRICAL

### Power and battery runtime

### Battery sizing

Two cells in series give 7.2 V nominal, 8.4 V at full charge, and 2.5 Ah. Series connection raises voltage, not amp-hours. Each cell is about 18.35 x 65 mm. The pack is approximately 18.5 x 130 mm end-to-end, or 37 x 65 mm side-by-side, before insulation and connection allowances. (Ref. 1, 2)

Nominal energy = 7.2 V x 2.5 Ah = 18 Wh

Favorable usable energy = 18 x 0.90 = 16.2 Wh

Planning usable energy = 18 x 0.80 = 14.4 Wh

| Mode | Battery power | Current at 7.2 V | Current at 6.4 V |
| --- | --- | --- | --- |
| Liquid | 20 W | 2.78 A | 3.13 A |
| Powder | 50 W | 6.94 A | 7.81 A |

Use 6.4 V under-load pack cutoff as an initial controller target, with per-cell protection in the BMS. The 90% usable-energy assumption is favorable and may not be achieved at that cutoff. The 80% allowance provides the planning case, while 90% defines the favorable runtime scenario.

| Energy budget | Liquid cumulative on-time | Powder cumulative on-time |
| --- | --- | --- |
| Favorable: 16.2 Wh | 0.81 h / 48.6 min | 0.324 h / 19.4 min |
| Planning: 14.4 Wh | 0.72 h / 43.2 min | 0.288 h / 17.3 min |

Runtime = usable Wh / battery watts. At 10% heating duty and 0.1 W assumed standby, favorable elapsed runtime is 16.2 / (0.1 x 20 + 0.9 x 0.1) = 7.75 h liquid, or 16.2 / (0.1 x 50 + 0.9 x 0.1) = 3.18 h powder. These are energy limits, not continuous thermal-duty ratings.

### Favorable modeled treatments per charge

| Diameter | Liquid | Powder |
| --- | --- | --- |
| 4 mm | About 1,695 at 1.72 s | About 200 at 5.82 s |
| 8 mm | About 152 at 19.14 s | About 17 at 66.95 s |

Cycles = 16.2 x 3,600 / (P x time). Counts omit standby, rework, transfer delays and additional dwell. Powder coating cool-down and application time are separate from heating time. An already warm screw requires a different heating duration.

### Two-mode power-control architecture

Pack/BMS -> MP8771 regulated supply -> ZVS inverter -> copper coil. STM32 reads a battery-voltage divider and INA180/shunt, calculates battery watts, and adjusts converter feedback through a DAC. It also controls a power switch, countdown and cutoff. At an assumed 90% converter efficiency, 50 W battery input means 45 W inverter input, or 9 A at 5 V. That is electrically within the converter’s documented 10 A capability, subject to PCB thermal design. (Ref. 3, 7, 9)

The ZVS board needs at least 5 V and has no documented wattage regulation. If its loaded power at 5 V is above 20 W, the proposed regulator cannot produce liquid mode merely by lowering voltage. If it cannot absorb 45 W within the available voltage range, powder mode also fails. These constraints define the required coil-load and converter operating range. Power control is specified through the regulated supply rather than assumed rapid supply PWM.


## NYLOK HANDHELD HEATER / 04 / PROTOTYPE BOM

### One prototype: purchase budget

### A. Basic heating test assembly

| Part | Qty | Cost | Basis |
| --- | --- | --- | --- |
| 2 EVE 25P cells (Ref. 1) | 2 x $3.99 | $7.98 | Listed |
| ZVS board + supplied coil (Ref. 3) | 1 | $2.75 | Listed |
| 2S 20 A BMS (Ref. 4) | 1 | $0.43 | Listed |
| 8.4 V charger module (Ref. 5) | 1 | $1.25 | Listed |
| High-current holder or pack interconnect | 1 set | $1.20 | Est. |
| Main power switch, DC >=10 A | 1 | $0.60 | Est. |
| Fuse and holder, initial 10 A target | 1 set | $0.50 | Est. |
| 18 AWG wire and electrical insulation | 1 set | $1.10 | Est. |
| Ceramic coil guard/support | 1 | $1.25 | Est. |
| Heat spreader / heatsink allowance | 1 | $1.00 | Est. |

Basic assembly subtotal: $18.06. Verified listed items total $12.41; accessories add $5.65 in estimated allocated cost. Small parts may require minimum packs, so cash checkout can be higher. This version uses manual operation and external measurement. It has no regulated two-mode control or countdown.

### B. Add two-mode control and countdown

| Additional part, one each | Cost | Basis |
| --- | --- | --- |
| MP8771GQ-P converter IC (Ref. 6, 7) | $2.61 | Listed |
| STM32G030F6P6 controller (Ref. 8) | $1.23 | Est. |
| INA180A2 current amplifier (Ref. 9) | $0.75 | Est. |
| 5 milliohm shunt, >=1 W | $0.15 | Est. |
| MCP4725 DAC (Ref. 10) | $1.27 | Est. |
| 3.3 V regulator and bypass parts | $0.30 | Est. |
| Converter inductor/capacitors | $1.50 | Est. |
| Feedback divider/filter components | $0.50 | Est. |
| Custom controller PCB | $2.00 | Est. |
| 0.96 inch OLED countdown display (Ref. 11) | $2.50 | Listed* |
| Power MOSFET and gate-drive parts | $0.35 | Est. |
| Mode/start buttons and status LED | $0.15 | Est. |

Control/display addition: $13.31. Complete parts allocation: $31.37. *Display price is listed; bulk display cost is estimated. The display is OLED, not LCD. Estimates are not verified purchasable single-item quotes. This parts allocation covers the proposed control architecture; the converter supporting components are grouped as an allowance.

The budget includes converter supporting components and a supplied induction coil. A custom narrow-band coil or different resonant capacitors would be a separate design-cost adjustment. Tools, programmer and instruments are excluded from the prototype prices.


## NYLOK HANDHELD HEATER / 05 / PRODUCTION

### Per-unit pricing at a 5,000-unit order

Across prototype and production cost groups, estimates were informed by multiple supplier searches and comparisons of available component prices and quantity tiers. Where public pricing was unavailable or a manufacturer quotation would be required, engineering allowances were used. These are budget estimates, not confirmed manufacturing quotations.

Prices below are per heater at an order quantity of 5,000. The basic version is manually operated; the two-mode version adds regulated power control, sensing and a countdown display. Both share the same battery pack, ZVS board, BMS and charger.

| Cost group | Basic | Two-mode | Pricing basis |
| --- | --- | --- | --- |
| Two EVE 25P cells | $4.00 | $4.00 | Estimated $2 per cell |
| ZVS board with coil (Ref. 3) | $2.42 | $2.42 | Public 1,000+ price retained |
| BMS (Ref. 4) | $0.39 | $0.39 | Public 5,000+ price |
| Charger module (Ref. 5) | $1.08 | $1.08 | Public 1,000+ price retained |
| Holder, switch, fuse, wire, ceramic and cooling | $1.57 | $1.57 | Estimate |
| MP8771 converter IC (Ref. 6) | $0.00 | $1.335 | Public 5,000 price |
| MCU, sense amp, shunt, DAC and 3.3 V supply | $0.00 | $1.83 | Estimate |
| Converter parts, feedback, PCB, MOSFET and controls | $0.00 | $1.35 | Estimate |
| OLED countdown display | $0.00 | $1.20 | Estimate |
| Parts subtotal | $9.46 | $15.175 | Listed prices + estimates |
| Housing | $1.20 | $1.20 | Estimate; tooling excluded |
| Assembly and pack integration | $1.00 | $1.00 | Equal allowance for comparison |
| Functional test and calibration | $0.50 | $0.50 | Equal allowance for comparison |
| Packaging | $0.35 | $0.35 | Estimate |
| Subtotal before reserve | $12.51 | $18.225 | Calculated |
| 5% scrap/rework allowance | $0.626 | $0.911 | Estimated reserve |
| Manufacturing cost per heater | $13.14 | $19.14 | Calculated estimate |

Basic heater: ($9.46 parts + $3.05 housing/assembly/test/packaging) x 1.05 = $13.14 per heater.

Two-mode heater: ($15.17505 parts + $3.05 housing/assembly/test/packaging) x 1.05 = $19.14 per heater.

Two-mode upgrade at this quantity: approximately $6.00 more per heater. Values are rounded; identical finishing-cost allowances make the comparison consistent.

These estimates apply to separate 5,000-unit orders for each version. They do not assume a mixed order of 2,500 basic and 2,500 two-mode heaters. Public 1,000-unit prices are retained at 5,000 without inventing further discounts. (Ref. 3-6)

### Budget boundaries and sensitivity

Prototype prices of $18.06 basic and $31.37 two-mode cover parts only and exclude the CAD housing. The production prices above include the estimated housing, assembly, functional test, packaging and reserve. This difference in scope should be retained when comparing prototype and production costs.

Both versions use an estimated $2 per battery cell. At $3 per cell, manufacturing cost rises by about $2.10 per heater after reserve: approximately $15.24 basic and $21.24 two-mode. Finishing costs use equal allowances; actual factory quotations may differ by version.

Freight, tariffs, tax, engineering, firmware, compliance testing, injection-mold tooling and sales costs are excluded. Any one-time development or tooling expense would be allocated separately across the 5,000 units. No profit margin is included. These are purchasing estimates, not fixed supplier quotations.


## NYLOK HANDHELD HEATER / 06 / REFERENCES

### Sources and pricing references

Sources checked October 3, 2026. Click a source title to open the supplier or manufacturer page. Prices and stock can change. BOM numbers refer to these entries.

(Ref. 1) [EVE 25P purchase listing](https://18650battery.com/products/eve-25p-18650-2500mah-30a-battery)

2,500 mAh, 3.6 V, 20 A retailer continuous rating; $3.99 per cell and in stock when checked.

(Ref. 2) [EVE manufacturer specification](https://www.evemall.com/consumer-battery/cylindrical-cell/18650-25p)

Cell dimensions and electrical specifications. Manufacturer maximum current has a temperature cutoff condition.

(Ref. 3) [ZVS induction board and supplied coil](https://electropeak.com/5v-12v-zvs-induction-heating-power-supply-module)

$2.75 single; $2.42 at 1,000+. 5-12 V input, 60 x 39 mm board. Advertised 120 W maximum is not an output guarantee.

(Ref. 4) [2S 20 A BMS](https://electropeak.com/2s-7-4v-20a-bms-18650-lithium-battery-protection-board)

$0.43 single; $0.39 at 5,000+. Verify balancing version and load-temperature performance.

(Ref. 5) [2S charging module](https://electropeak.com/2-strings-8-4v-lithium-battery-charging-module)

$1.25 single; $1.08 at 1,000+. Configure for two lithium-ion cells and 8.4 V.

(Ref. 6) [MP8771 purchase listing](https://www.digikey.com/en/products/detail/monolithic-power-systems-inc/MP8771GQ-P/8769462)

$2.61 single and $1.33505 at 5,000 from the retrieved distributor price schedule; confirm at checkout.

(Ref. 7) [MP8771 manufacturer and datasheet](https://www.monolithicpower.com/en/mp8771.html)

3-18 V input, 10 A output capability, enable and protection features. Supporting components and PCB layout are required.

(Ref. 8) [STM32G030F6P6 procurement reference](https://www.lcsc.com/product-detail/C724040.html)

Controller candidate. $1.23 prototype line is an allowance based on the retrieved related TR listing, not a locked quotation.

(Ref. 9) [INA180 manufacturer information](https://www.ti.com/product/INA180)

Current-sense amplifier. Use A2 gain of 50 with a 5 milliohm shunt; price in the BOM is an estimate.

(Ref. 10) [MCP4725 procurement reference](https://www.digikey.com/en/products/detail/microchip-technology/MCP4725A1T-E-CH/1827895)

DAC candidate for converter feedback control. $1.27 is a budget allowance based on a retrieved related ordering variant.

(Ref. 11) [Low-cost countdown display](https://www.elexp.com/collections/new-collection/products/0-96-oled-iic-display-module-header-pin-not-soldered)

$2.50 listed price, SKU 08OLED-HNS. OLED rather than LCD; would still need to confirm supply/interface and availability before ordering.
