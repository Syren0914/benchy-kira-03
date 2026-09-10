# Open-source license proposal

**Proposal only.** This file records a recommended approach; it does not apply a license to hardware files that have not been supplied or to third-party material.

For a project intended to be widely buildable and modifiable, a practical permissive starting point is:

| Material | Proposed license | Scope |
|---|---|---|
| Original hardware/interconnection design and enclosure CAD | CERN-OHL-P-2.0 | Original design source and associated hardware design documentation as explicitly identified |
| Original firmware, if present | MIT | Code owned by the project author; preserve dependency licenses |
| Original guide prose and photographs | CC BY 4.0 | Original instructional/media content, with attribution |

CERN OHL v2 offers permissive, weakly reciprocal, and strongly reciprocal variants. If the creator wants downstream hardware modifications to remain under reciprocal conditions, evaluate W or S rather than automatically using P. Read the official text for the selected variant. [CERN Open Hardware Licence](https://cern-ohl.web.cern.ch/home).

CC BY 4.0 permits sharing and adaptation with attribution and its other conditions. Only apply it to content the creator is entitled to license. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

MIT is a permissive software license with notice requirements. Use the actual license text and correct copyright holder information if firmware is included. [MIT text](https://choosealicense.com/licenses/mit/).

## Before adopting the proposal

- Confirm the author/copyright holder name and which files are original.
- Inventory purchased modules and document their interfaces, part numbers, manuals, and availability. Buying a module does not grant permission to relicense its firmware or internal circuit design.
- Identify borrowed CAD, schematics, code, fonts, logos, decorative graphics, photographs, and music. Preserve their notices and check redistribution rights.
- Copy the selected official license texts into LICENSES and add a root license map identifying which paths each license covers.
- Include a third-party notices file that identifies the source, author, license, and modifications for each reused item.
- Do not claim OSHWA certification unless it has been obtained.

Open-source hardware requires useful design documentation in an editable form and licensing that permits the relevant reuse. Simply making a folder publicly viewable is not enough. [OSHWA definition](https://oshwa.org/definition/).
