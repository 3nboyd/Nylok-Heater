# Handheld induction heater: research and engineering model

Prepared for the Notre Dame / Marmon / Nylok Innovate-a-thon, October 3, 2026.

## Recommended development configuration

Develop a **100 W battery-side input prototype for carbon-steel fasteners**, using an existing nominal 18 V tool battery, a documented low-voltage resonant induction driver, an insulated copper work coil, and closed-loop screw-temperature measurement. Use wired laboratory power first. Keep the sleeve application process separate: heat, switch off, withdraw the coil, then place the sleeve.

This is a system architecture and sizing study, not a fabrication-ready schematic or demonstrated heater. The missing piece for exact component selection is the measured loaded coil impedance and achievable power transfer into representative screws. No specific switching transistors, tank capacitor ratings, PCB trace widths, or coil current limits should be signed off from the thermal calculation alone.

The 65°C and 250°C targets used below are illustrative calculation points. They are **not confirmed Nylok application temperatures**. Exact chemistry, allowable overshoot, dwell and transfer time remain unknown. The main base case is a 10 g effective heated steel mass initially at 25°C.

## 1. Existing-system evidence and material choice

Induction Innovations lists solid copper coils on its Mini-Ductor II. Its instructions recommend closely fitting, evenly wound coils with clearance from the workpiece and describe forming 3–4 turns. Its Bearing Buddy product is described as flexible litz wire. These are established construction patterns, not evidence that a small copied coil will match the original driver's performance. [1–3]

| Coil material | Appropriate role | Decision |
|---|---|---|
| Solid copper conductor | Simple formed work coil with replaceable head | First geometry prototype |
| Copper litz wire | Flexible head and reduced high-frequency copper loss when properly specified | Second comparison prototype |
| Copper tube | Higher-current coil with provision for cooling | Consider if solid-wire temperature becomes limiting |
| Ordinary steel wire | High resistance and undesirable heating of the conductor | Do not use for the work coil |
| Rope or ordinary cord | Appearance mockup only | No electrical function |

Litz uses individually insulated strands with a deliberate construction. Ordinary stranded cable is not equivalent. New England Wire identifies operating frequency as an input to strand-gauge and construction selection. [4]

**Starting head geometry, for an 8 mm diameter screw:**

- Four turns of 2 mm diameter copper conductor.
- Insulation build giving approximately 3 mm finished wire diameter, subject to the insulation supplier's actual dimensions and ratings.
- 10 mm clear insulated bore, leaving nominal 1 mm radial clearance to a centered 8 mm screw.
- 3.5 mm axial turn-center pitch, leaving nominal 0.5 mm between adjacent insulated turns.
- Approximately 13.5 mm axial span.
- Short, closely routed outgoing/return leads, keeping the resonant power stage near the head.
- Ceramic positioning/support pieces and a guard that does not introduce an uncharacterized conductive loop near the coil.

Use purpose-rated high-temperature electrical insulation, such as a qualified glass-fiber/ceramic sleeve system. Specify dielectric strength, temperature, abrasion and chemical resistance. Do not substitute ordinary tape. Manufacturer coil guidance establishes the need for insulation and clearance; it does not establish an exact insulation recipe for our head. [2]

The copper coil can heat through its own electrical loss and through radiation from the screw. Induction does not mean the coil stays cold. Test short repeated bursts and measure coil temperature before claiming an operating duty cycle.

## 2. Physics of induction

Battery DC powers a high-frequency inverter. Alternating current in the copper coil creates a changing magnetic field. That field induces circulating eddy currents in the screw; electrical resistance converts their energy into heat. Ferromagnetic material can also exhibit hysteresis losses. A steady DC coil produces no sustained induction heating after the transient.

The first-principles relationships are:

\[\oint E\cdot dl=-d\Phi_B/dt\]

\[J=\sigma E,\qquad p=J\cdot E=J^2/\sigma\]

The workpiece behaves like a lossy, coupled secondary. Coil-to-part coupling and reflected resistance depend on geometry, material and frequency. A short screw differs considerably from a cooking pan or a bolt-removal tool, so their published efficiencies cannot be copied into this project. ST AN4713 explains the resonant coil/load architecture and frequency-dependent power regulation. [5]

**Starting frequency investigation:** approximately 100–200 kHz, as a design-search range rather than a selected frequency. The suitable value depends on loaded inductance, workpiece resistance, coil loss and driver switching loss.

### Skin depth

\[\delta=\sqrt{\rho/(\pi f\mu_0\mu_r)}\]

Illustrative material inputs at 100 kHz:

| Material assumptions | Calculated skin depth |
|---|---:|
| Copper: resistivity 1.72e−8 Ωm, relative permeability 1 | 0.209 mm |
| Example magnetic steel: resistivity 1.5e−7 Ωm, relative permeability 100 | 0.0616 mm |
| Example nonmagnetic stainless: resistivity 7e−7 Ωm, relative permeability 1 | 1.33 mm |

These resistivities/permeabilities are illustrative screening inputs, not measured values for the challenge's screws. Steel permeability changes with field, grade, frequency and temperature. At 200 kHz, these depths decrease by a factor of square-root two.

Skin depth identifies where current concentrates initially. **Do not budget heat only for this thin skin.** Heat conducts into the body while the heater runs and after it stops.

### Coil field, inductance and resonance

A long-solenoid screening relationship is:

\[B\approx\mu_0NI/\ell\]

Our short coil requires an end correction and a workpiece model. Increasing turns or current changes field, but it also changes inductance, copper loss and driver loading. It does not provide a universal power formula.

An unloaded long-solenoid approximation gives:

\[L\approx\mu_0N^2 A_{coil}/\ell\]

For four turns, mean conductor radius about 6.5 mm and length about 13.5 mm, this gives approximately **0.20 µH**. This short-coil approximation is crude. Lead inductance, finite geometry and the inserted steel can materially change the value. Measure both unloaded and loaded impedance at the intended frequency.

\[f_0=1/(2\pi\sqrt{LC})\]

If measured effective L were 0.20 µH, resonance would require about 12.7 µF at 100 kHz or 3.17 µF at 200 kHz. These are arithmetic examples, **not capacitor selections**. Resonant RMS current, reactive voltage, temperature, ESR and topology determine capacitor-bank construction and rating. Low DC supply voltage does not imply low resonant stress.

Circulating coil current can be much larger than battery current. For example, a 100 W input draws about 5.6 A at nominal 18 V, while a tank might circulate tens of amperes. The latter must be established by measurement and circuit analysis. At an illustrative 40 A RMS and 3 mΩ AC coil resistance, copper loss is 4.8 W. Skin/proximity effects and warm copper can increase resistance.

## 3. Coil coverage and actual thermal mass

For N turns, center pitch p and finished wire diameter D:

\[L_{span}=(N-1)p+D\]

For the proposed geometry, Lspan = 13.5 mm. The cylindrical envelope opposite an 8 mm screw is:

\[A_{band}=\pi dL_{span}=339\text{ mm}^2\]

This is a geometric reference area. The coil has **zero intended contact area with the screw**. Magnetic fields overlap between turns and extend beyond the head. Copper-wire thickness does not carve a sharply bounded heated band.

A solid cylindrical segment of that length and diameter has volume679 mm³ and, at an assumed steel density7.85 g/cm³, mass5.33 g. Actual threaded volume differs. At cp0.5 J/g/K, heating this segment from25°C to250°C would require about600 J if thermally isolated.

It is not thermally isolated. The rest of the screw, head and holder absorb heat. The base system model therefore uses10 g effective mass. We must calibrate that against temperature measurements near and away from the coil.

For an illustrative carbon-steel thermal diffusivity1.2e−5 m²/s, the diffusion length scale sqrt(alpha*t) is about17 mm over24 seconds. This is a scale estimate, not a sharp boundary or validated temperature profile. Nonuniform initial heating and colder adjacent metal can shorten the sleeve-placement window considerably.

The sleeve/stencil defines **coating location**. The heater prepares a region that may be wider. A1–2 thread coating band does not require a1–2 thread electromagnetic footprint.

## 4. Thermal model with external factors

The supplied calculator numerically integrates:

\[mc\,dT/dt=(P_{battery}-P_{controls})\eta_{conversion}\eta_{coupling}-hA(T-T_a)-\epsilon\sigma_{SB}A(T_K^4-T_{a,K}^4)-G(T-T_a)\]

| Input | Base assumption | Meaning |
|---|---:|---|
| Effective heated mass |10 g| Not necessarily the full fastener mass |
| Specific heat |0.5 J/g/K| Constant screening approximation |
| Ambient / target |25°C /250°C| Illustrative temperatures |
| Battery-side power |100 W| Includes controls |
| Controls |1 W| Also consumed between shots |
| Conversion efficiency |90%| Combined electrical-conversion assumption |
| Coupling fraction |60%| Electrical output transferred to modeled metal |
| Exposed screw area |12 cm²| Total modeled hot area, not only339mm² band |
| Convection coefficient |25 W/m²/K| Example mild-airflow assumption |
| Emissivity |0.3| Finish-dependent assumption |
| Holder conductance |0.02 W/K| Simplified loss path to an ambient-temperature holder |
| Usable battery fraction |80%| Reserve/aging/cold allowance, separate from conversion |

The model places53.46 W into the metal before environmental/holder losses. At250°C it loses about6.75 W to convection,1.37 W to radiation and4.5 W through the holder. Approximate instantaneous net heating power at that point is40.8 W.

Base sensible heat is1,125 J. The numerical model adds about153 J of external/holder loss during heating, reaches the target in23.9s and draws about0.664 Wh for that heating cycle.

### Predicted scenarios

| Scenario | Calculated time | Total cycle energy |
|---|---:|---:|
|5 g effective mass|11.6s|0.32Wh|
|10 g effective mass|23.9s|0.66Wh|
|30 g effective mass|79.9s|2.22Wh|
|10 g, illustrative65°C target|3.8s|0.11Wh|
|10 g, h raised to75 W/m²/K|28.7s|0.80Wh|
|10 g,0°C ambient and h75|33.5s|0.93Wh|
|10 g, coupling reduced from60% to30%|56.4s|1.57Wh|

Mass comparisons use exposed area proportional to mass^(2/3), a simplified similar-shape comparison. These are not measured times and do not promise uniform temperature. The controller must also deal with sensor lag and overshoot, especially in the short65°C example.

### Model limits

- No coating-specific dwell or reheating is included.
- No sleeve thermal mass or transfer enthalpy is included.
- No evaporation of a wet screw or active rain is included. Wet fasteners require separate treatment.
- No battery-voltage sag model or tank-impedance calculation is included.
- Constant material properties approximate the temperature range.
- A lumped node does not predict along-screw gradients or all surface temperatures.
- The effective holder-loss path must be fitted to actual hardware.
- Repeated coil/electronics temperature rise can impose cooldown time even if battery energy remains.

Use the thermal model for energy and runtime sizing. Use instrumented tests or electromagnetic/thermal simulation for coupling, gradients and heater limits.

## 5. Battery energy, mAh and hours of use

\[E_{rated}(Wh)=V_{nominal}\times mAh/1000\]

An18 V,5,000 mAh pack contains nominal90 Wh. DEWALT identifies its20V MAX* platform as18 V nominal; use nominal voltage in the energy calculation. [6]

At80% usable capacity, the model has72 Wh available. Conversion losses are handled in the heating model and are not subtracted a second time from this capacity allowance.

\[P_{avg}=P_{controls}+R\,E_{incremental\ heating}\]

R is screws/hour; incremental heating energy excludes continuous controls to avoid double counting. For the base screw it is0.658 Wh/screw.

| Base screw usage |Average power|Work time,18V5Ah|Approximate screws/charge|
|---|---:|---:|---:|
|15/hour|10.9W|6.6h|99|
|30/hour|20.7W|3.5h|104|
|60/hour|40.5W|1.8h|107|
|Continuous100W draw|100W|43.2minutes|Not a throughput claim|

Lower-throughput operation wastes more capacity in the continuously powered controls. Sleep/off-between-use can improve that part of the budget. Tool thermal duty must independently support the requested throughput.

At30 screws/hour, the model requires about2.88 Ah at18 V for2h and5.76 Ah for4h. An18 V8 Ah pack would model about5.6h at that throughput. Under the weak-coupling case, a5Ah pack models about1.5h at30/hour. Capacity alone does not establish discharge-current capability.

**Why a510 battery is not the selected source:** the thread standard specifies an interface, not a power rating. A hypothetical3.7 V650mAh battery has only2.4Wh rated energy and would need roughly27A to supply100W before additional losses. This example is not the specification of Noah's actual battery. We need its label, continuous output rating and cutoff behavior before considering it.

### Existing-power routes

1. **Laboratory isolated current-limited DC supply:** first driver and coil measurements. Compatible voltage/current depend on the chosen documented driver.
2. **Tool battery through a manufacturer PD adapter:** DEWALT DCB094 supports up to100W output. Negotiate a supported profile and verify actual100W delivery, startup and overload behavior. [7] Keep the high-frequency tank near the coil, not at the belt-end of a long HF cable.
3. **Direct tool-battery input:** final compact version, only with a compatible interface and implemented pack/tool protection requirements. A plastic slide adapter alone does not establish undervoltage or thermal protection.

For USB-C at20V,100W means5A. Use a5A-rated electronically marked cable and proper PD negotiation. Adapter output power and battery-side input differ due to adapter loss; the100W battery-side base budget can keep tool output below the adapter's ceiling. Do not promise100W to the screw.

## 6. System architecture and future KiCad PCB

Power path: existing battery/interface -> input protection/current sensing -> compatible low-voltage resonant inverter -> tank capacitor bank -> short coil leads -> insulated work coil.

Measurement/control path: insulated screw-contact thermocouple -> conditioning/converter -> MCU -> driver power command; MCU also operates LCD and reads profile knob/trigger. Monitor the work-head/power-stage temperature independently.

### Candidate blocks

|Block|Development choice|Selection condition|
|---|---|---|
|MCU|STM32-class or similarly capable3.3V controller|Enough timers/SPI/ADC, watchdog and documented driver interface|
|Screw sensor|Electrically insulated, small K-type contact junction|Required temperature, response and repeatable surface contact|
|Thermocouple interface|MAX31856 candidate|SPI, cold-junction compensation, fault handling; RF environment verification|
|Display|Small LCD with actual/target/status|Display is not the sensor|
|Selector|Rotary encoder or detented knob|Select coating recipe; do not present voltage as temperature|
|Power stage|Documented low-voltage resonant module initially|100W-class actual input control, intended tiny-coil L/load compatibility|
|Coil connector|Mechanically keyed low-loss high-current connection|Measured tank current, frequency, contact heating and insulation|

MAX31856 is a real thermocouple converter candidate, with line-frequency filtering and fault detection. Its50/60Hz filtering does not guarantee rejection of100–200kHz induction interference. Analog Devices cautions against grounded-tip use. Use an appropriately isolated junction, short twisted sensor leads, physical separation and input filtering. Verify readings with the inverter enabled and disabled; quiet sampling windows may be needed. [8–9]

Do not choose an IR sensor only because it avoids contact. Small shiny threaded surfaces introduce emissivity, reflection and field-of-view problems. Fluke identifies adjustable emissivity as important for metal measurements. [10]

### Control behavior

On power-up, verify head, supply and sensor. Trigger starts a current-limited heating cycle. Near the selected target, reduce power using the driver's documented control scheme. Assert READY only after validated sensing and any required dwell. Shut down on overtemperature, overcurrent, lost sensor, missing/incorrect head or timeout. Display a valid transfer window only after cooling tests support it.

Voltage alone does not set temperature. Use closed-loop temperature control. A resonant driver may regulate through frequency, controlled bursts or bus voltage; the chosen topology determines the allowable method. Do not add arbitrary series PWM to an undocumented self-oscillating board. ST's high-voltage IGBT cooker examples explain principles but are not low-voltage component selections. [5]

Keep resonant high-current loops small, capacitor paths short and sensing separated from switching nodes. Fuse and current-limit settings, MOSFET voltage/current margin, driver deadtime, capacitor RMS rating, conductor/connector sizing and heatsink design require loaded-circuit testing. MCU current limiting alone does not protect fast faults; use appropriate hardware shutdown.

## 7. Tightening knob and interchangeable heads

A closer coil generally improves coupling, but maintain a physical gap. Manufacturer instructions explicitly avoid coil-to-metal contact. [2]

For the first working prototype, use **fixed S/M/L coil heads with a knob that locks the head and centers the workpiece**. This retains a simple adjustment while avoiding continuous unknown retuning.

For a later true diameter-adjusting head, the knob must move an insulated flexible coil through a mechanically limited range, preserve turn count/separation and clearance, and operate only with power off. Test the entire adjustment range with the driver. Changes to coil shape alter L, coupling, resonance and possible circulating current. An automatic impedance/tuning routine or restricted calibrated positions may be required.

Specify usable fastener diameters per head, not only nominal S/M/L labels. For a radial clearance g, clear bore must be at least fastener diameter+2g, plus manufacturing/alignment allowance. Head diameters may exceed shank diameters, requiring an opening coil or insertion from the screw tip. Split coils create another high-frequency connector problem; they are not automatically the simpler option.

Support nonmagnetic screws mechanically. Carbon steel is the initial induction-validation material. Austenitic stainless, brass and aluminum need separate driver/coil tests and may require a different head or another heating method. Do not equate nonmagnetic with electrically nonconductive, or promise universal heating with one recipe.

## 8. Measurements that complete the design

1. Weigh representative screws and record material, plating, diameter, head shape and length.
2. Measure each coil's unloaded/loaded inductance and resistance at intended frequencies, not just with DC or a low-frequency meter.
3. Measure battery-side energy per shot and coil/tank current with suitable equipment.
4. Measure temperature at the center band, both band edges, head and remote shaft.
5. Repeat for head sizes, clearances, ambient conditions and consecutive-shot duty.
6. After shutdown, measure cooling at0.5s intervals during real sleeve positioning. Derive the practical transfer window.
7. Confirm sensor error/lag against an independent reference, including during RF operation.
8. Test final coating transfer and function. A correct heater reading is not proof of coating performance.

Measure effective thermal mass and coupling instead of fitting both arbitrarily: use spatial temperature measurements and energy logging to constrain them. One heating-time measurement cannot uniquely identify all the loss parameters.

## Presentation wording

“An18V5,000mAh battery stores about90Wh. Our illustrative100W model uses about0.66Wh to heat a10g steel screw, including assumed losses. At30 screws per hour, that is about3.5hours per charge. Coil coupling and outdoor conditions will determine the measured result.”

Use the editable one-slide deliverable and calculator. Say **estimated/modelled**, not demonstrated. Do not describe the250°C example as the confirmed product recipe.

## Primary sources

1. Induction Innovations, Mini-Ductor II: https://www.theinductor.com/product/mini-ductor-ii/
2. Induction Innovations, coil usage/clearance: https://www.theinductor.com/blog/how-to-properly-use-induction-heating-coils/
3. Induction Innovations, flexible litz example: https://www.theinductor.com/blog/how-to-get-more-out-of-your-mini-ductor-induction-heater/
4. New England Wire, litz engineering: https://litzwire.com/litz-wire-design-engineering/
5. STMicroelectronics AN4713: https://www.st.com/resource/en/application_note/an4713-induction-cooking--igbts-in-resonant-converters-stmicroelectronics.pdf
6. DEWALT5Ah pack and18V nominal: https://www.dewalt.com/en-us/product/dcb205c/20v-max-5ah-starter-kit
7. DEWALT100W PD adapter: https://www.dewalt.com/en-us/product/dcb094k/20v-max-flexvolt-5-amp-usb-charging-kit
8. Analog Devices MAX31856: https://www.analog.com/en/products/max31856.html
9. Analog Devices grounded-tip guidance: https://ez.analog.com/data_converters/a/documents/c/max31856-faq/DO12495/is-it-possible-to-use-maxim-s-thermocouple-to-digital-converter-with-grounded-thermocouple
10. Fluke emissivity: https://www.flukeprocessinstruments.com/en-us/why-use-pyrometers%3F/emissivity-metals

All unreferenced numerical design inputs above are explicit engineering assumptions or calculations, not supplier specifications. Actual coating temperature, chemistry and allowed carrier residue remain outside the supplied information.
