import os
import shutil
import subprocess
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject,
    DecodedStreamObject,
    DictionaryObject,
    FloatObject,
    NameObject,
    NumberObject,
    TextStringObject,
)


ROOT = Path(__file__).resolve().parent
DOCX_SOURCE = ROOT / "docs" / "Benchy_Kira_03_Project_Review_Brief.docx"
BASE_DIR = ROOT / "tmp" / "pdfs" / "base"
SOURCE = BASE_DIR / "Benchy_Kira_03_Project_Review_Brief.pdf"
OUTPUT = ROOT / "docs" / "Benchy_Kira_03_Project_Review_Brief.pdf"
FORM_PAGE = 3  # zero-based page containing the reviewer form
PAGE_WIDTH = 612.0
PAGE_HEIGHT = 792.0
# Calibration reference: the visually inspected 1376 x 1780 page render.
PIXEL_WIDTH = 1376.0
PIXEL_HEIGHT = 1780.0


def build_base_pdf():
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    local_soffice = (
        ROOT
        / "LibreOffice_26.8.0.3_Machine_X64_msi_en-US"
        / "SourceDir"
        / "LibreOffice"
        / "program"
        / "soffice.exe"
    )
    configured = os.environ.get("SOFFICE_PATH")
    soffice = configured or shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice and local_soffice.exists():
        soffice = str(local_soffice)
    if not soffice:
        raise RuntimeError("LibreOffice is required. Install it or set SOFFICE_PATH.")

    profile = ROOT / "tmp" / "lo-profile-fillable"
    shutil.rmtree(profile, ignore_errors=True)
    SOURCE.unlink(missing_ok=True)
    subprocess.run(
        [
            str(soffice),
            f"-env:UserInstallation={profile.resolve().as_uri()}",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(BASE_DIR),
            str(DOCX_SOURCE),
        ],
        check=True,
    )
    if not SOURCE.exists():
        raise RuntimeError(f"LibreOffice did not create {SOURCE}")


def rect_from_pixels(x1, y1, x2, y2):
    sx = PAGE_WIDTH / PIXEL_WIDTH
    sy = PAGE_HEIGHT / PIXEL_HEIGHT
    return [x1 * sx, PAGE_HEIGHT - y2 * sy, x2 * sx, PAGE_HEIGHT - y1 * sy]


def blank_appearance(writer, width, height):
    stream = DecodedStreamObject()
    stream.set_data(
        f"q 0.18 0.42 0.68 RG 0.75 w 0.5 0.5 {max(width - 1, 0):.2f} {max(height - 1, 0):.2f} re S Q".encode("ascii")
    )
    stream.update(
        {
            NameObject("/Type"): NameObject("/XObject"),
            NameObject("/Subtype"): NameObject("/Form"),
            NameObject("/BBox"): ArrayObject(
                [FloatObject(0), FloatObject(0), FloatObject(width), FloatObject(height)]
            ),
            NameObject("/Resources"): DictionaryObject(),
        }
    )
    return writer._add_object(stream)


def add_widget(writer, fields, name, rect, *, multiline=False, options=None, tooltip=None):
    x1, y1, x2, y2 = rect
    appearance = blank_appearance(writer, x2 - x1, y2 - y1)
    widget = {
        "/Type": "/Annot",
        "/Subtype": "/Widget",
        "/FT": "/Ch" if options else "/Tx",
        "/T": name,
        "/TU": tooltip or name.replace("_", " ").title(),
        "/Rect": rect,
        "/F": 4,
        "/V": "",
        "/DV": "",
        "/DA": "/Helv 9 Tf 0 g",
        "/Q": 0,
        "/BS": {"/W": 0.75, "/S": "/S"},
        "/MK": {"/BC": [0.18, 0.42, 0.68]},
        "/AP": {"/N": appearance},
    }
    if multiline:
        widget["/Ff"] = 4096
    if options:
        widget["/Ff"] = 131072
        widget["/Opt"] = options
    inserted = writer.add_annotation(FORM_PAGE, widget)
    fields.append(inserted.indirect_reference)


build_base_pdf()
reader = PdfReader(SOURCE)
if len(reader.pages) != 4:
    raise ValueError(f"Expected four pages, found {len(reader.pages)}")

writer = PdfWriter()
writer.clone_document_from_reader(reader)

font = DictionaryObject(
    {
        NameObject("/Type"): NameObject("/Font"),
        NameObject("/Subtype"): NameObject("/Type1"),
        NameObject("/BaseFont"): NameObject("/Helvetica"),
        NameObject("/Encoding"): NameObject("/WinAnsiEncoding"),
    }
)
font_ref = writer._add_object(font)
fields = ArrayObject()
acroform = DictionaryObject(
    {
        NameObject("/Fields"): fields,
        NameObject("/DA"): TextStringObject("/Helv 9 Tf 0 g"),
        NameObject("/DR"): DictionaryObject(
            {NameObject("/Font"): DictionaryObject({NameObject("/Helv"): font_ref})}
        ),
        NameObject("/NeedAppearances"): NameObject("/false"),
    }
)
writer.root_object[NameObject("/AcroForm")] = writer._add_object(acroform)

add_widget(writer, fields, "reviewer_name", rect_from_pixels(280, 190, 710, 235), tooltip="Reviewer name")
add_widget(writer, fields, "review_date", rect_from_pixels(780, 190, 1020, 235), tooltip="Review date")

rows = [
    (338, 430, "problem_definition"),
    (451, 543, "technical_design"),
    (565, 657, "testing_evidence"),
    (678, 770, "safety_practice"),
    (791, 883, "documentation"),
    (905, 997, "overall_direction"),
]
for y1, y2, key in rows:
    add_widget(
        writer,
        fields,
        f"assessment_{key}",
        rect_from_pixels(510, y1, 865, y2),
        options=["", "Strong", "Adequate", "Revise"],
        tooltip=f"Assessment - {key.replace('_', ' ')}",
    )
    add_widget(
        writer,
        fields,
        f"comments_{key}",
        rect_from_pixels(885, y1, 1235, y2),
        multiline=True,
        tooltip=f"Comments - {key.replace('_', ' ')}",
    )

for index, (y1, y2) in enumerate(((1060, 1112), (1118, 1170), (1178, 1230)), start=1):
    add_widget(
        writer,
        fields,
        f"priority_{index}",
        rect_from_pixels(150, y1, 1055, y2),
        tooltip=f"Priority recommendation {index}",
    )

add_widget(
    writer,
    fields,
    "additional_comments",
    rect_from_pixels(128, 1282, 1080, 1515),
    multiline=True,
    tooltip="Additional comments",
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("wb") as stream:
    writer.write(stream)

expected_names = {
    "reviewer_name",
    "review_date",
    "additional_comments",
    "priority_1",
    "priority_2",
    "priority_3",
}
for _, _, key in rows:
    expected_names.add(f"assessment_{key}")
    expected_names.add(f"comments_{key}")

check = PdfReader(OUTPUT)
found = check.get_fields() or {}
missing = expected_names - set(found)
unexpected = set(found) - expected_names
if missing or unexpected:
    raise ValueError(f"Field mismatch; missing={sorted(missing)}, unexpected={sorted(unexpected)}")

widgets = []
for page in check.pages:
    for ref in page.get("/Annots", []):
        annot = ref.get_object()
        if annot.get("/Subtype") == "/Widget":
            widgets.append(annot)
if len(widgets) != len(expected_names):
    raise ValueError(f"Expected {len(expected_names)} widgets, found {len(widgets)}")
for widget in widgets:
    if widget.get("/V", "") != "":
        raise ValueError(f"Unexpected initial value in {widget.get('/T')}")
    normal = (widget.get("/AP") or {}).get("/N")
    if normal is None or not normal.get_object().get_data():
        raise ValueError(f"Missing appearance stream for {widget.get('/T')}")

# Exercise representative field types in a temporary copy so the delivered
# blank form is known to accept and preserve text, multiline text, and choices.
test_values = {
    "reviewer_name": "Test Reviewer",
    "review_date": "2026-09-10",
    "assessment_problem_definition": "Strong",
    "comments_problem_definition": "Clear objective and motivation.",
    "priority_1": "Confirm the complete wiring map.",
    "additional_comments": "Electronic form-field validation copy.",
}
test_writer = PdfWriter()
test_writer.clone_document_from_reader(check)
test_writer.update_page_form_field_values(None, test_values, auto_regenerate=False)
test_path = ROOT / "tmp" / "pdfs" / "fillable-field-test.pdf"
test_path.parent.mkdir(parents=True, exist_ok=True)
with test_path.open("wb") as stream:
    test_writer.write(stream)

test_check = PdfReader(test_path)
test_fields = test_check.get_fields() or {}
for name, expected in test_values.items():
    actual = test_fields[name].get("/V", "")
    if actual != expected:
        raise ValueError(f"Test value mismatch for {name}: {actual!r} != {expected!r}")
for page in test_check.pages:
    for ref in page.get("/Annots", []):
        widget = ref.get_object()
        name = widget.get("/T")
        if widget.get("/Subtype") == "/Widget" and name in test_values:
            normal = (widget.get("/AP") or {}).get("/N")
            if normal is None or not normal.get_object().get_data():
                raise ValueError(f"Filled widget lacks an appearance stream: {name}")

print(f"Created {OUTPUT} with {len(expected_names)} validated interactive fields")
