# Benchy — Kira 03 parts list

Source: creator's direct description on 2026-09-09, supplemented by visible exterior features. This is a useful procurement draft; it is not yet an exact shopping list.

## Creator-confirmed components

| Item | Quantity | Confirmed information | Still required for a repeatable build |
|---|---|---|---|
| PLA filament | Determine from validated slicing | PLA used for enclosure | Brand/grade, color allocation, mass, print profile |
| M3 screws | Not provided | M3 diameter family | Count, length, head type, thread/insert/nut arrangement, locations |
| M2 screws | Not provided | M2 diameter family | Count, length, head type, thread/insert/nut arrangement, locations |
| SK120 module | 1 implied; verify | Creator identifies SK120 | Manufacturer/full model/revision, manual, pinout, installed limits |
| Old computer power supply | 1 implied; verify | Reused computer PSU | Model, dimensions, input/rail ratings, connectors, condition, compatibility |
| Arduino Nano | 1 implied; verify | Nano used | Exact board/clone/processor, supply connection, pin map, sketch |
| Relay | 1 implied; verify | Relay used | Bare relay versus module, model, coil/input voltage, drive polarity, contact ratings, switched circuit |

## Visible or required integration details to inventory

The photos also show connectors/terminals, a rear inlet/switch arrangement, and front controls. Some may be included with the PSU or SK120; others may be separate purchases. Confirm whether the yellow question-mark item is a button cap and identify the switch beneath it. List output sockets, the upper yellow connector, mating plugs, wiring, terminations, insulation, and retention parts explicitly, even if salvaged from an existing assembly.

## Compatibility notes

An “old computer PSU” is not a universal drop-in part. Different units can differ in dimensions, connector conventions, rail ratings, control signals, and load behavior. The release should identify one tested model and explain the checks needed for alternatives. Do not use wire color alone to establish a pinout.

Do not equate the SK120 name or a vendor's maximum rating with KIRA's usable output. The assembled limit depends on the actual module, source voltage/current, losses, wiring, connectors, and cooling. In particular, higher output voltage through a converter does not imply the same available output current.

The Nano family has variants with different features and pinouts. Link the documentation for the actual board after it is identified. [Official Nano family overview](https://support.arduino.cc/hc/en-us/articles/11264980365468-Nano-family-overview).

The relay's purpose must be established before documenting its wiring. A power-enable signal, a DC output, and a mains conductor require very different designs and ratings. Do not invent a Nano pin assignment, relay contact selection, or startup state.

## Cost record

Record local currency, purchase date, supplier, unit cost, shipping, and quantities. Separate the cost of reused parts already owned from the replacement cost for a new builder. No budget estimate is claimed in this draft.
