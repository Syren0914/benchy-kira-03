# Enclosure model

[Download/open the supplied 3MF](power%20supply%20v.2.3mf)

![Embedded preview from the supplied 3MF](../docs/images/model-preview.png)

The creator identified this file in Downloads as the enclosure source for the project. It was copied here unchanged. The preview above is the archive's own thumbnail, not a newly generated rendering or proof of printability.

## Inspection results

- File: `power supply v.2.3mf` (2,679,250 bytes).
- Declared units: millimeters.
- Embedded title: `power supply v.2 (v1~recovered)`.
- 74 mesh objects and 74 build items, with no non-identity build-item transforms.
- 177,806 triangles in total.
- Main named objects: `Backside`, `Face`, and `Middle`; the remaining objects use Body names.
- Combined mesh extents in file coordinates: approximately **108.53 × 182.00 × 222.50 mm** along X/Y/Z.
- The preview shows KIRA 03 markings and geometry resembling the photographed enclosure.

These are mesh bounds, not independently measured assembled-product dimensions. Object count is not a screw count or a count of separately printed pieces. Some objects may represent lettering or other details; retain their relationships until reviewed in CAD/slicer software.

The archive contains a model, thumbnail, content-type information, and relationships. No slicer print-settings file, G-code, firmware, schematic, or parametric CAD history was found in it. Mesh parsing does not establish manifoldness, clearances, material suitability, or successful slicing.

## Manufacturing guide

1. Open the 3MF in a compatible slicer as a multipart model, preserving its object positions and millimeter units.
2. Compare the preview and named objects with the actual assembly. Identify which bodies form one part, lettering/color regions, and which must be separated for printing.
3. Review scale against actual modules and connectors. Do not auto-scale to fit a printer.
4. Prepare the Face, Middle, and Backside using validated print orientations. Do not print the entire assembled-position model as one object without reviewing its geometry.
5. Assign the creator-confirmed PLA material, then establish printer-specific nozzle, layer height, walls, infill, support, and temperature settings through fit and thermal validation.
6. Print a critical fit sample first where practical. Check display fit, connector holes, fasteners, and panel alignment against actual components.
7. Inspect the finished parts and dry-fit them with power disconnected. Record orientation, support removal, part mass, print duration, and any dimensional compensation used.
8. Publish the validated slicer project alongside this model, including printer, nozzle, material, and profile versions. Publish editable CAD/STEP if available for easier changes to fit another PSU.

The creator confirmed M2 and M3 screws, but counts, lengths, head types, and nut/insert arrangements are not yet provided. Do not infer them from nominal screw diameter alone.

PLA is the creator's material choice, not a verified thermal/fire rating for the electrical assembly. Assess temperatures and enclosure suitability using the final load and airflow arrangement.
