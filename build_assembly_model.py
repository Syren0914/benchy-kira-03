"""Build the Benchy - Kira 03 visual assembly model.

Combines the printed enclosure (mechanical/power supply v.2.3mf) with
reference models of the internal hardware:

* XY-SK120 buck-boost module (third-party OBJ, placed in the display window)
* a generic ATX computer PSU (150 x 86 x 140 mm, 80 mm rear fan, IEC inlet)
* an XT60 panel-mount female connector (top of the front panel)
* banana jacks, the yellow "?" button and the indicator lens

The internal parts are visual stand-ins sized from public standard dimensions
(ATX PSU, XT60E) and from the cut-outs in the enclosure. They are NOT
measured from the creator's actual donor PSU. Use them for renders, fit
checks and the product video, not as manufacturing references.

Coordinate frame of the outputs: millimetres, +Y up, front panel facing +Z
(the source 3MF is stored upside down, so it is rotated 180 deg about Z).

Requires: pip install trimesh numpy shapely manifold3d scipy matplotlib
Run:      python build_assembly_model.py
"""

from pathlib import Path

import numpy as np
import shapely
import trimesh
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath
from shapely.geometry import Point, Polygon, box

ROOT = Path(__file__).resolve().parent
ENCLOSURE = ROOT / "mechanical" / "power supply v.2.3mf"
SK120_OBJ = ROOT / "mechanical" / "third-party" / "xy-sk120" / "xy-sk120.obj"
OUT = ROOT / "mechanical" / "assembly"

# ---- colours (RGBA) -------------------------------------------------------
WHITE_PLA = (236, 233, 224, 255)
BLACK_PLA = (22, 22, 24, 255)
PSU_STEEL = (34, 34, 37, 255)
PSU_DARK = (14, 14, 15, 255)
NICKEL = (190, 192, 196, 255)
BRASS = (214, 170, 72, 255)
XT60_YELLOW = (240, 178, 32, 255)
BUTTON_YELLOW = (246, 196, 30, 255)
LABEL_SILVER = (200, 202, 206, 255)
RED = (200, 30, 30, 255)
ORANGE = (235, 120, 20, 255)
YELLOW_WIRE = (235, 205, 30, 255)

# ---- key positions measured from the enclosure cut-outs (corrected frame) --
PANEL_FRONT_Z = 217.0          # outer face of the front panel
PANEL_BACK_Z = 207.0           # inner face of the front panel
DISPLAY_CENTRE = (0.0, 34.5)   # 76.6 x 40 mm window
XT60_CENTRE = (0.0, 65.9)      # 19 x 13 mm window, M2.5 screws at x = +/-12.5
JACKS = {                      # banana jack centres
    "12V": (-18.5, -11.3), "3V3": (-18.5, -31.3), "5V": (-18.5, -51.3),
    "COM": (2.0, -31.3), "ADJ+": (25.0, -75.0), "ADJ-": (42.0, -75.0),
}
BUTTON_CENTRE = (25.4, -6.6)   # 14 x 14 mm
LED_CENTRE = (25.5, -28.4)     # 9 x 3.3 mm slot
PSU_W, PSU_H, PSU_D = 86.0, 150.0, 140.0  # ATX, standing on its side


def colour(mesh, rgba):
    mesh.visual.face_colors = np.tile(rgba, (len(mesh.faces), 1))
    return mesh


def extrude(poly, z0, z1, rgba):
    polys = list(poly.geoms) if hasattr(poly, "geoms") else [poly]
    m = trimesh.util.concatenate([trimesh.creation.extrude_polygon(p, z1 - z0) for p in polys])
    m.apply_translation([0, 0, z0])
    return colour(m, rgba)


def rrect(cx, cy, w, h, r):
    return box(cx - w / 2 + r, cy - h / 2 + r, cx + w / 2 - r, cy + h / 2 - r).buffer(r, 16)


def cyl(cx, cy, r, z0, z1, rgba, sections=48):
    return extrude(Point(cx, cy).buffer(r, sections // 4), z0, z1, rgba)


def text_poly(text, size, cx, cy):
    tp = TextPath((0, 0), text, size=size, prop=FontProperties(family="DejaVu Sans", weight="bold"))
    polys = [Polygon(p) for p in tp.to_polygons() if len(p) > 2]
    out = None
    for p in sorted(polys, key=lambda p: -p.area):  # even-odd fill
        p = p.buffer(0)
        out = p if out is None else (out.difference(p) if out.contains(p) else out.union(p))
    minx, miny, maxx, maxy = out.bounds
    return shapely.affinity.translate(out, cx - (minx + maxx) / 2, cy - (miny + maxy) / 2)


def tube(points, r, rgba):
    """Wire along a polyline: cylinders between points plus joint spheres."""
    parts = []
    for a, b in zip(points[:-1], points[1:]):
        parts.append(trimesh.creation.cylinder(radius=r, segment=[a, b], sections=12))
    for p in points[1:-1]:
        s = trimesh.creation.icosphere(subdivisions=1, radius=r)
        s.apply_translation(p)
        parts.append(s)
    return colour(trimesh.util.concatenate(parts), rgba)


def bezier(p0, p1, p2, p3, n=18):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2, p3 = map(np.asarray, (p0, p1, p2, p3))
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


# ---- enclosure ------------------------------------------------------------
def load_enclosure():
    src = trimesh.load(ENCLOSURE, force="scene")
    flip = trimesh.transformations.rotation_matrix(np.pi, [0, 0, 1])
    parts = {}
    for name, g in src.geometry.items():
        g = g.copy()
        g.apply_transform(flip)
        # small bodies sunk into the front face are the black text/graphic inlays
        inlay = name.startswith("Body") and g.bounds[0][2] > 200
        parts[f"enclosure/{name}"] = colour(g, BLACK_PLA if inlay else WHITE_PLA)
    return parts


# ---- XY-SK120 -------------------------------------------------------------
def load_sk120():
    src = trimesh.load(SK120_OBJ, force="scene")  # Fusion export, centimetres
    parts = {}
    for i, (name, g) in enumerate(src.geometry.items()):
        g = g.copy()
        # geometries are split per material, named like "Opaque(232,173,35)"
        try:
            rgba = [int(v) for v in name[name.index("(") + 1:name.index(")")].split(",")] + [255]
        except ValueError:
            rgba = [160, 160, 160, 255]
        g.apply_scale(10.0)
        # bezel flange spans OBJ z 0..2.5 mm, so OBJ z=0 sits on the panel face
        g.apply_translation([DISPLAY_CENTRE[0], DISPLAY_CENTRE[1], PANEL_FRONT_Z])
        parts[f"sk120/{i:02d}"] = colour(g, rgba)
    return parts


# ---- ATX PSU --------------------------------------------------------------
def build_psu():
    w, h, d = PSU_W, PSU_H, PSU_D
    z0, z1 = 0.0, d  # rear sits on the back panel (z=0), front meets the bulkhead (z=140)
    r = 3.0
    fan_c, fan_r = (0.0, 36.0), 39.0
    parts = {}

    shell = extrude(rrect(0, 0, w, h, r), z0 + 1.2, z1, PSU_STEEL)
    rear = rrect(0, 0, w, h, r).difference(Point(*fan_c).buffer(fan_r, 32))
    parts["psu/housing"] = trimesh.util.concatenate([shell, extrude(rear, z0, z0 + 1.2, PSU_STEEL)])

    # 80 mm fan behind the rear grille
    fan = [cyl(*fan_c, fan_r, z0 + 6, z0 + 7, PSU_DARK), cyl(*fan_c, 13, z0 + 1.5, z0 + 6, PSU_DARK)]
    for k in range(7):
        a = 2 * np.pi * k / 7
        blade = Polygon([(13, -5), (37, -9), (37, 7), (13, 5)])
        blade = shapely.affinity.rotate(blade, np.degrees(a), origin=(0, 0))
        blade = shapely.affinity.translate(blade, *fan_c)
        b = extrude(blade, z0 + 2.5, z0 + 4.5, PSU_DARK)
        fan.append(b)
    parts["psu/fan"] = trimesh.util.concatenate(fan)

    grille = []
    for rr in (10, 18, 26, 34, 38.5):
        ring = Point(*fan_c).buffer(rr + 0.8, 32).difference(Point(*fan_c).buffer(rr - 0.8, 32))
        grille.append(extrude(ring, z0, z0 + 1.2, NICKEL))
    for ang in (0, 60, 120):
        bar = shapely.affinity.rotate(box(-fan_r, -0.8, fan_r, 0.8), ang, origin=(0, 0))
        grille.append(extrude(shapely.affinity.translate(bar, *fan_c), z0, z0 + 1.2, NICKEL))
    parts["psu/fan_guard"] = trimesh.util.concatenate(grille)

    # IEC C14 inlet and rocker switch, visible through the lower rear window
    iec_c = (-9.0, -50.0)
    iec_outline = rrect(*iec_c, 20, 27, 2).difference(
        Polygon([(iec_c[0] - 10, iec_c[1] + 13.5), (iec_c[0] - 10, iec_c[1] + 8),
                 (iec_c[0] - 4.5, iec_c[1] + 13.5)]))
    iec_cav = rrect(iec_c[0], iec_c[1] - 1, 15, 20, 1.5)
    inlet = [extrude(iec_outline.difference(iec_cav), z0, z0 + 4, BLACK_PLA),
             extrude(iec_cav, z0 + 3, z0 + 4, PSU_DARK)]
    for px, py in ((-4, -4), (4, -4), (0, 3)):
        inlet.append(extrude(box(iec_c[0] + px - 2, iec_c[1] + py - 0.8, iec_c[0] + px + 2, iec_c[1] + py + 0.8),
                             z0 + 1, z0 + 4, NICKEL))
    parts["psu/iec_inlet"] = trimesh.util.concatenate(inlet)
    sw_c = (18.0, -50.0)
    parts["psu/switch"] = trimesh.util.concatenate([
        extrude(rrect(*sw_c, 14, 21, 1.5), z0, z0 + 2, BLACK_PLA),
        extrude(rrect(sw_c[0], sw_c[1] + 3, 10, 9, 1), z0, z0 + 1, RED),
    ])

    # label on the +X side, visible through the side vents and the X truss
    lab = trimesh.creation.box([0.3, 120, 100])
    lab.apply_translation([w / 2 + 0.15, 0, z0 + 70])
    parts["psu/label"] = colour(lab, LABEL_SILVER)
    stripe = trimesh.creation.box([0.35, 120, 12])
    stripe.apply_translation([w / 2 + 0.2, 0, z0 + 28])
    parts["psu/label_stripe"] = colour(stripe, XT60_YELLOW)

    # cable grommet on the front face
    parts["psu/grommet"] = cyl(0, -45, 9, z1, z1 + 5, PSU_DARK)
    return parts


# ---- XT60 panel mount (female) --------------------------------------------
def build_xt60():
    cx, cy = XT60_CENTRE
    zf = PANEL_FRONT_Z
    flange = rrect(cx, cy, 31.0, 12.0, 2.0)
    for sx in (-12.5, 12.5):
        flange = flange.difference(Point(cx + sx, cy).buffer(1.4, 12))
    # D-shaped housing: two chamfered corners mark the polarity
    hw, hh, c = 7.9, 4.1, 2.2
    dshape = Polygon([(cx - hw, cy - hh), (cx + hw - c, cy - hh), (cx + hw, cy - hh + c),
                      (cx + hw, cy + hh - c), (cx + hw - c, cy + hh), (cx - hw, cy + hh)])
    parts = {
        "xt60/flange": extrude(flange, zf, zf + 2.0, XT60_YELLOW),
        "xt60/housing": extrude(dshape.difference(dshape.buffer(-1.0)), zf + 2.0, zf + 4.5, XT60_YELLOW),
        "xt60/face": extrude(dshape.buffer(-1.0), zf + 2.0, zf + 3.2, XT60_YELLOW),
        "xt60/body": extrude(dshape, zf - 14.0, zf, XT60_YELLOW),
    }
    contacts = []
    for sx in (-3.6, 3.6):
        contacts.append(cyl(cx + sx, cy, 2.1, zf + 3.0, zf + 3.4, BRASS, 32))
        contacts.append(cyl(cx + sx, cy, 1.3, zf + 3.1, zf + 3.5, PSU_DARK, 32))
        contacts.append(cyl(cx + sx, cy, 1.8, zf - 20.0, zf - 14.0, BRASS, 24))
    parts["xt60/contacts"] = trimesh.util.concatenate(contacts)
    screws = [cyl(cx + sx, cy, 2.2, zf + 2.0, zf + 3.2, NICKEL, 24) for sx in (-12.5, 12.5)]
    parts["xt60/screws"] = trimesh.util.concatenate(screws)
    return parts


# ---- front-panel hardware -------------------------------------------------
def build_panel_hardware():
    zf = PANEL_FRONT_Z
    jacks = []
    for name, (x, y) in JACKS.items():
        jacks += [cyl(x, y, 4.4, zf - 18, zf, NICKEL, 32),
                  cyl(x, y, 5.6, zf, zf + 2.2, BLACK_PLA, 40),
                  cyl(x, y, 2.6, zf + 2.2, zf + 2.6, NICKEL, 32),
                  cyl(x, y, 2.0, zf + 2.3, zf + 2.7, PSU_DARK, 32)]
    parts = {"panel/jacks": trimesh.util.concatenate(jacks)}

    bx, by = BUTTON_CENTRE
    parts["panel/button"] = extrude(rrect(bx, by, 13.4, 13.4, 1.2), zf - 6, zf + 8, BUTTON_YELLOW)
    parts["panel/button_mark"] = extrude(text_poly("?", 9.5, bx, by), zf + 8, zf + 8.4, (250, 250, 250, 255))
    lx, ly = LED_CENTRE
    parts["panel/led_lens"] = extrude(rrect(lx, ly, 8.6, 3.0, 1.45), zf - 3, zf + 0.6, (235, 240, 245, 255))
    return parts


# ---- internal wiring (illustrative only) ----------------------------------
def build_wiring():
    g = np.array([0, -45, PSU_D + 5.0])  # grommet passes the 70 x 60 bulkhead opening
    runs = [  # (colour, end point) - PSU rails to the fixed jacks and SK120 input
        (YELLOW_WIRE, (-18.5, -11.3, 199)), (ORANGE, (-18.5, -31.3, 199)),
        (RED, (-18.5, -51.3, 199)), (BLACK_PLA, (2.0, -31.3, 199)),
        (YELLOW_WIRE, (-12.0, 20.0, 174)), (BLACK_PLA, (-6.0, 20.0, 174)),
    ]
    wires = []
    for i, (rgba, end) in enumerate(runs):
        start = g + np.array([(i - 2.5) * 2.2, 0, 0])
        end = np.array(end, float)
        pts = bezier(start, start + [0, 0, 20], end - [0, 0, 18], end)
        wires.append(tube(pts, 1.0, rgba))
    # SK120 output to the adjustable jacks and the XT60
    for rgba, end in ((RED, (25.0, -75.0, 199)), (BLACK_PLA, (42.0, -75.0, 199)),
                      (RED, (-3.6, 65.9, 197)), (BLACK_PLA, (3.6, 65.9, 197))):
        start = np.array([24.0 if rgba == RED else 30.0, 20.0, 174.0])
        end = np.array(end, float)
        pts = bezier(start, start - [0, 0, 8], end - [0, 0, 16], end)
        wires.append(tube(pts, 0.9, rgba))
    return {"wiring/harness": trimesh.util.concatenate(wires)}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    groups = {
        "enclosure": load_enclosure(),
        "sk120": load_sk120(),
        "psu": build_psu(),
        "xt60": build_xt60(),
        "panel": build_panel_hardware(),
        "wiring": build_wiring(),
    }
    scene = trimesh.Scene()
    for group in groups.values():
        for name, mesh in group.items():
            scene.add_geometry(mesh, node_name=name, geom_name=name)

    scene.export(OUT / "benchy_kira03_assembly.glb")
    for key in ("psu", "xt60"):
        merged = trimesh.util.concatenate(list(groups[key].values()))
        merged.export(OUT / f"{key}_reference.stl")
    print("bounds", np.round(scene.bounds, 1).tolist())
    for key, group in groups.items():
        merged = trimesh.util.concatenate(list(group.values()))
        print(f"{key:10s}", np.round(merged.bounds, 1).tolist())
    return groups


if __name__ == "__main__":
    main()
