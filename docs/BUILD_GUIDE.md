# Benchy — Kira 03 — project documentation and build guide

**Revision:** documentation draft 0.1 • 2026-09-09
**Build status:** incomplete engineering inputs; not ready for independent construction.

## 1. Project purpose

Benchy is a compact bench power-supply project intended to be shared so that other makers can understand, reproduce, repair, and modify it. Desktop computers have become more power-hungry, so a power supply that was adequate ten years ago may no longer meet the demands of a modern computer. That does not mean the older supply has stopped working. Rather than discard functional hardware, the project repurposes it as the basis of a bench supply for electronics work, prototyping, and testing. The photographed prototype combines a vertically arranged front panel with a display, knob, labeled terminals, and a framed enclosure.

The documentation must explain both what to do and how to verify that each stage is correct. Appearance alone does not establish safe construction, electrical capability, or compliance.

## 2. Evidence and boundaries

The source set is 40 HEIC photographs, IMG_1245 through IMG_1284, in the creator's [Drive folder](https://drive.google.com/drive/folders/1a5vY3R4KkWWrwnvo-AKPjcpfRcpAucLN). The gallery was visually reviewed, with larger previews inspected for IMG_1258, IMG_1253, and IMG_1262. These show the exterior, not the internal circuit. The creator subsequently supplied power supply v.2.3mf and identified PLA, M2/M3 screws, SK120, a reused computer PSU, Arduino Nano, and a relay. See [parts list](PARTS_LIST.md) and [enclosure inspection](../mechanical/README.md).

| Item | Current evidence | What must be supplied |
|---|---|---|
| Public identity | Creator confirms Benchy — Kira 03 | Version subsequent hardware changes separately |
| Input | Rear inlet and switch visible | Supply model, permitted input range/frequency, fuse and protective design |
| Fixed outputs | Labels: 12V, 3.3V, 5.0V | Actual measured voltages, current limits, shared power budget |
| Display/control | Creator identifies SK120; controls visible | Exact manufacturer/revision, manual, settings, operating sequence |
| Other connectors | Yellow upper connector; lower +/− pair | Part numbers, polarity, circuit function, permissible loads |
| Grounding | Exterior cannot establish it | Verified schematic for PE, chassis, DC returns, and output isolation |
| Enclosure | PLA confirmed; 3MF included | Parametric source if available, validated slicer settings, screw details |
| Firmware | Reference Nano relay-module test sketch supplied | Exact board and relay module, hardware bias, final switched circuit, and as-built behavior |
| Performance | No test record | Regulation, ripple, thermal, protection, and combined-load results |

Do not identify a commercial module from its faceplate alone. Visually similar modules can have different pinouts and specifications.

## 3. Intended audience and prerequisites

The completed guide should support builders who can read a schematic, identify connector pin numbering, use a multimeter correctly, and assemble the specified mechanical parts. Mains construction and protective testing require appropriate competence and equipment. A beginner may contribute enclosure work and documentation while having the electrical design and assembly reviewed by a qualified person.

Before buying parts, select one released hardware revision. Do not mix CAD, wiring, and BOM files from different revisions without a documented compatibility note.

## 4. Specification sheet to complete

Record a value, its source, and its conditions for every specification. Use “not tested” where appropriate.

| Specification | Value now | Required conditions/source |
|---|---|---|
| Input voltage and frequency | Unverified | Exact manufacturer data and installed configuration |
| Fixed output voltages/tolerance | Unverified | Measurement at terminals, no load and rated load |
| Current available on each output | Unverified | Continuous limit and simultaneous-load restrictions |
| Adjustable output range, if present | Unverified | Verified module, input headroom, output load |
| Total continuous output power | Unverified | All outputs combined, ambient temperature and duration |
| Current limiting | Unverified | Which outputs support it, range, behavior, recovery |
| Output isolation/common return | Unverified | Schematic and suitable verification |
| Ripple/noise | Unverified | Load, bandwidth, probe method, measurement location |
| Thermal performance | Unverified | Ambient, enclosure closed, airflow, load, temperatures |
| Size and mass | Unverified | Dimensions of final assembled unit |
| Build cost and time | Unverified | Dated local pricing; include tools, shipping, print failures |

Keep supplier maximum ratings separate from demonstrated system ratings. The sum of channel ratings must not be presented as simultaneously available unless it has been established for the entire system.

## 5. Source and manufacturing files

Use the following target layout when engineering sources arrive. The mechanical 3MF and preview are now included; other engineering files remain planned.

```text
hardware/     editable schematic, PCB if used, wiring diagram, fabrication exports
mechanical/   editable enclosure CAD, STEP, STL/3MF or dimensioned cut drawings
bom/          verified parts list and dated sourcing notes
firmware/     source, tool versions, dependencies, build and flashing procedure, if needed
docs/images/  selected web images and assembly photographs
tests/        procedures, raw measurements, equipment details, result summaries
LICENSES/     adopted license texts and third-party notices
```

Publish editable source as well as fabrication outputs. A rendered schematic or STL alone may let someone inspect or manufacture a part, but does not provide the preferred editable source needed to modify the design. See the [OSHWA definition](https://oshwa.org/definition/).

## 6. Bill of materials requirements

The BOM must include quantity, reference designator or assembly location, manufacturer, exact part number, essential ratings, dimensions, approved alternatives, supplier, dated price, and notes. Include small but necessary items: spacers, screws, inserts, feet, terminals, wire, insulation, strain relief, labels, fuses, and mating connectors.

Inventory to identify from the actual unit:

| Assembly group | Information required |
|---|---|
| Main supply | Manufacturer/model, intact module versus custom circuit, output ratings and connector details |
| Display/regulator | Exact model/revision and manufacturer manual |
| Input assembly | Inlet/switch/fuse arrangement and component ratings |
| Output terminals | Type, hole size, panel thickness range, electrical ratings, mating plugs |
| Upper yellow connector | Exact type, mounting method, purpose and polarity |
| Question-mark control | Electrical function, component behind it, cap attachment |
| Enclosure | Every separate part, material, process, revision, quantity |
| Cooling | Fan or passive arrangement, guards, supply wiring, airflow direction |
| Wiring and fasteners | Gauge, insulation, termination, lengths, screw lengths and torque where specified |

Do not substitute merely because a product looks similar. Evaluate electrical ratings, polarity, thermal requirements, mechanical fit, and mounting clearances, then document the approved alternative.

## 7. Circuit and wiring documentation

A [preliminary connection schematic](../hardware/CONNECTION_SCHEMATIC.md) now records the intended low-voltage module architecture and flags every unconfirmed Nano, relay, and PSU-enable connection as TBC. It is not a build-ready schematic. The definitive revision must show the complete input path, protective measures, each conversion stage, control connections, and every output return. If an intact commercial power module is used, distinguish its internal proprietary design from KIRA's original interconnection and mechanical work.

Create one wiring-schedule row per conductor:

| Wire ID | From connector/pin | To connector/pin | Function | Gauge/insulation | Color | Length | Terminations | Verification |
|---|---|---|---|---|---|---|---|---|
| To be assigned | Required | Required | Required | Required | Required | Required | Required | Required |

Every connector drawing must state whether it is viewed from the mating face or wire side. Show positive, negative, protective earth, chassis, sense lines, and enable/control signals explicitly. Never use color as the only identifier. Explain whether returns are shared or isolated and whether any output can be connected in series; do not assume either behavior.

## 8. Mechanical preparation

Once verified CAD and process settings are available:

1. Match every part to the selected hardware revision and inspect dimensions against its drawing.
2. Manufacture a small fit-check piece for critical connector or insert features before committing to the full enclosure, where practical.
3. Remove debris and inspect edges, mounting holes, cracks, and deformation.
4. Dry-fit the enclosure, panels, modules, connectors, and fasteners with no power connected.
5. Verify that fasteners cannot contact circuitry and that vents, guards, and insulation barriers are unobstructed.
6. Use the creator-confirmed PLA material and record validated printer settings. The supplied 3MF has no stored slicer profile; do not invent layer height, infill, temperatures, or print orientation.

The release must supply part orientation, manufacturing tolerances, support requirements if printed, fastener lengths, and assembly order. Enclosure thermal and fire suitability must be established for this application.

## 9. Electrical assembly — completion gate

**Stop here until the verified BOM, schematic, wiring schedule, and protective design exist.** The steps below define the documentation workflow; they are not a substitute wiring procedure.

1. Photograph and identify each module and its connector labels before mounting.
2. Install components following the validated mechanical order and manufacturer requirements.
3. Route and terminate the wiring exactly as the approved schedule specifies. Document separation of hazardous and accessible circuits, mechanical retention, and insulation.
4. Photograph each stage before the next assembly conceals it. Include connector orientation and wire IDs.
5. Have the completed wiring and protective measures reviewed against the schematic before energizing.

Do not open or modify the mains circuitry inside a commercial supply to follow an undocumented assumption. The public guide must explicitly state which modules remain intact and what work is required.

## 10. Inspection and commissioning

The project designer must define suitable equipment, safe setup, test points, numerical acceptance limits, and the responsible reviewer. Protective testing must use methods appropriate to the installed design and applicable requirements; an ordinary continuity beep does not establish electrical safety.

### Before power

- Verify component identities, polarity, conductor endpoints, terminations, fastener retention, and absence of loose conductive debris.
- Verify the specified input protection, protective-earth/chassis arrangement where required, barriers, and strain relief.
- Check required insulation and separation using the approved procedure.
- Confirm that ventilation and fan guards are unobstructed and no accessible live parts remain.
- Record inspection results and resolve failures before power is applied.

### Electrical measurements

Only after the safety review, use the approved commissioning setup. Establish no-load operation before increasing loads within verified component limits. Record external meter measurements separately from the front-panel display. Test each output individually and then in documented combinations. Define safe protection tests before performing them; do not improvise a direct short circuit.

| Test | Record | Acceptance |
|---|---|---|
| No-load output | Terminal voltage and displayed value for each channel | Designer-defined limits |
| Load regulation | Setpoints, current, terminal voltage, duration | Designer-defined limits |
| Combined load | Every channel's load and total power | Verified shared budget |
| Current limit, if supported | Set value, measured behavior, recovery | Verified intended behavior |
| Ripple/noise | Scope settings, probe arrangement, load, trace | Designer-defined limits |
| Thermal | Ambient, enclosure state, load, fan behavior, temperatures | Limits for all installed materials/components |
| Power cycle | Startup/shutdown behavior and output state | Defined safe default state |
| Display accuracy | Reference instrument and errors over range | Declared tolerance |

Never connect a grounded oscilloscope probe to an unverified node. Establish the output reference and suitable measurement method first.

If there is an unexpected voltage, odor, smoke, abnormal heating, arcing, unstable output, or repeated protective trip, stop and isolate the input safely. Diagnose with power removed and stored energy addressed under the approved service procedure.

## 11. Operating guide — finalize against actual controls

The final operating guide must identify each control, output, status indicator, and power-up default. Until those facts are confirmed, this draft cannot give a valid button sequence.

For the released unit, explain how to select the correct output, set voltage/current where supported, verify polarity and voltage before attaching a device, enable or disable the output, and disconnect the load. State which terminals are always energized when the supply is on. Include examples using specified, tested loads.

Do not advertise battery charging, series/parallel outputs, motor handling, reverse-energy tolerance, or sensitive-device suitability unless those uses are designed for and verified. Explain any load types that require additional protection.

## 12. Troubleshooting

| Symptom | Initial safe action | What the completed guide should identify |
|---|---|---|
| Display dark | Disconnect input before opening | Power path, switch state, module supply, documented service checks |
| Display on but no output | Remove load; check documented output state | Enable function, limit/protection states, connector map |
| Incorrect voltage | Disconnect the device being powered | Correct terminal, mode, setpoint, external meter verification |
| Output falls under load | Reduce load within the verified envelope | Current limit, shared budget, wiring drop, source headroom |
| Excessive temperature | Stop operation and allow safe cooling | Airflow, fan operation, ambient/load limits, assembly faults |
| Protective device trips | Isolate input; do not repeatedly reset | Qualified fault diagnosis; replacement only with specified type |

These are diagnostic categories, not confirmed faults in the photographed prototype.

## 13. Maintenance and repair

Keep vents clear and inspect cables and connectors before use. Define the service isolation/discharge procedure using the actual supply manufacturer's information. Replace parts only with specified or validated alternatives. Repeat relevant inspection and electrical tests after changes. Record modifications as a new hardware revision when they affect compatibility or performance.

## 14. Independent reproduction

Before labeling a release “build-ready,” give its download archive to another builder. Have them record missing parts, ambiguous steps, undocumented tools, and deviations. Update the guide until the build and tests can be completed without private explanations from the creator.

## 15. Next information needed from the creator

The project name is confirmed as Benchy — Kira 03. Supply exact PSU/SK120/Nano/relay variants, schematic or conductor-by-conductor wiring notes, screw and connector details, interior assembly photos, manufacturing settings, Nano sketch and relay function, measured results, authorship/attribution details, and desired licensing approach. The enclosure 3MF and preliminary core parts list have already been supplied. These inputs convert this structured draft into a specific reproducible manual.
