# Benchy — Kira 03 — YouTube production kit

## Video concept

Tell the story of turning a personal bench tool into a project another maker can reproduce. Lead with the finished device, show the real construction, demonstrate measured behavior, then point viewers to a versioned build release.

**Suggested title now:** “I Built Benchy: My Kira 03 Bench Power Supply”
**Title after a complete licensed release exists:** “I Open-Sourced Benchy — Kira 03 — Build, Test & Files”

Use Benchy — Kira 03 consistently in the title and description. Avoid unmeasured voltage/current/power claims and “anyone can build this” until the documentation has passed an independent build.

## Storyboard and narration draft

The timings below are editing targets for a roughly 10-minute video, not timestamps for footage that already exists. Bracketed items require the creator's facts or new footage.

| Time | Picture | Narration / purpose |
|---|---|---|
| 0:00–0:20 | Full unit, knob detail, safe closed-case demonstration | “This is Benchy, my Kira 03 project, my custom bench power supply. I want to share more than the finished object: I want someone else to understand it and build their own version.” |
| 0:20–0:55 | Creator at workbench; original sketches if available | “The problem I wanted to solve was [your actual reason]. My priorities were [your real priorities].” Explain why this form factor exists. |
| 0:55–1:40 | Front and rear tour | Point out the display, controls, labeled terminals, inlet, and vents. Identify each function only after confirming it. State the public hardware revision. |
| 1:40–2:30 | Verified block diagram and module labels | “The design uses [exact supply] and [exact regulator/control module]. Here is what I designed and what comes from commercial modules.” Explain the actual power path. |
| 2:30–3:35 | CAD, parts, manufacturing, dry fitting | Show editable files, key dimensions, material/process, mounting, and the useful lessons from failed fits. |
| 3:35–5:05 | De-energized assembly, connector diagrams | Explain the verified wiring schedule and mechanical retention. Show protective measures in context. Do not speed through a critical connection without a clear diagram in the guide. |
| 5:05–5:45 | Inspection and closed enclosure | Explain who reviewed the electrical construction and what was checked. Avoid claiming certification unless it exists. |
| 5:45–7:25 | Meter, suitable load, actual test records | Show no-load and loaded readings, combined-load constraints, and any verified current-limit behavior. Keep setpoint, displayed value, and measured value distinct. |
| 7:25–8:10 | Enclosure/airflow and thermal results | “At [ambient] with [load] for [duration], I measured [results].” Discuss limits honestly. |
| 8:10–9:05 | Working demonstration and lessons | Show one intended use with a known suitable load. Explain one compromise and one improvement for the next revision. |
| 9:05–10:00 | Public repository and release archive | Show where to find the BOM, editable files, guide, license, and tests. Invite build reports with hardware revision and photographs. |

## Confirmed parts to show on camera

The creator identifies a PLA enclosure, M2/M3 screws, SK120, a reused computer PSU, Arduino Nano, and a relay. Show each actual part and the included 3MF. Explain the Nano and relay only after their function and wiring are confirmed. Do not imply that these core parts omit the necessary connectors and wiring from the complete BOM.

## Opening script you can use

“This is Benchy, my Kira 03 project, a bench power supply I built for my workspace. I gave it a compact enclosure and a front panel that puts the controls and connections together. Now I’m preparing the project for other makers. In this video I’ll show the design, the parts, the assembly, and the tests—and explain what you need before building one.”

## Closing script

Use after the release is complete:

“The exact files for the version in this video are linked below: the parts list, editable design files, wiring documentation, build guide, and test results. Read the safety section before starting. If you make one, share your hardware revision and what you changed. Those build reports will help improve the next version.”

If filming before release, say: “The documentation is still in progress. The project page lists what is available and what still needs verification.”

## Essential filming checklist

- Record clean, steady wide shots, then close-ups of every important connection and mounting feature.
- Capture module model labels in focus; the viewer should be able to match the BOM.
- Record electrical assembly with the unit safely disconnected; use diagrams to explain hazardous sections.
- Film operation with the enclosure closed and a reviewed test setup.
- Make display digits and external meter readings legible and avoid flicker where possible.
- Capture actual measurements and test conditions before writing performance claims.
- Record room tone and clear narration; choose music you have permission to use.
- Capture a thumbnail-specific landscape shot with space beside the product for text.
- Keep original footage and an edit copy; retain the hardware revision associated with each take.

## Thumbnail direction

Start from IMG_1258 for a concept: a large product view with short text, “MY BENCH PSU” or “BUILD KIRA.” Use “OPEN SOURCE” only when the licensed design source is actually public. Prefer a new powered shot if the screen can be made readable without altering the displayed measurement.

Keep the styling consistent with the object: off-white background, near-black text, small yellow accent. Do not add a glowing display, fake measurement, invented specifications, or certification badge.

## Description draft — after release

```text
Meet Benchy — Kira 03, my custom bench power-supply project.

This video covers the design, enclosure, assembly, and measured performance of hardware revision [REVISION].

BUILD FILES AND GUIDE
Versioned release: [PUBLIC RELEASE URL]
Project repository: [PUBLIC REPOSITORY URL]
Parts list: [PUBLIC BOM URL]
Wiring and build guide: [PUBLIC GUIDE URL]
Test results and limitations: [PUBLIC TEST REPORT URL]
Licenses and third-party credits: [PUBLIC LICENSE URL]

Electrical work requires appropriate skills. Read the guide's safety and commissioning sections before building. Use the files for the exact revision shown here.

CHAPTERS
[Replace with timestamps from the finished edit]

Share your build report and improvements through the repository's issue tracker.

Credits: [Design contributors, music, third-party sources]
```

## Pinned comment draft

“Start with release [version] linked in the description. Please check the current errata before building. For help, include your hardware revision, exact module models, and what you measured. Please do not post personal information.”

Do not publish until bracketed placeholders have been replaced and every public link works when signed out.
