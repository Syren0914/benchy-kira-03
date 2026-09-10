from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
PNG = ROOT / "hardware" / "nano-relay-test.png"
SVG = ROOT / "hardware" / "nano-relay-test.svg"

WIDTH, HEIGHT = 1600, 1000
NAVY = "#192A45"
BLUE = "#2F6EAD"
GREEN = "#2D7D46"
RED = "#C92F2F"
GRAY = "#667085"
LIGHT = "#F4F7FB"
YELLOW = "#FFF3CD"


def font(size, bold=False):
    paths = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for path in paths:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


img = Image.new("RGB", (WIDTH, HEIGHT), "white")
d = ImageDraw.Draw(img)

d.text((70, 44), "Benchy — Kira 03 • Arduino Nano + Relay Bench Test", fill=NAVY, font=font(42, True))
d.text((70, 100), "Reference low-energy connection • Relay contacts remain disconnected", fill=GRAY, font=font(24))

d.rounded_rectangle((70, 150, 1530, 245), radius=18, fill=YELLOW, outline="#C78A00", width=4)
d.text((95, 168), "SCOPE", fill=NAVY, font=font(25, True))
d.text((205, 168), "Use only with a verified 5 V logic-compatible relay module.", fill=NAVY, font=font(25))
d.text((205, 203), "Power the Nano by USB for this test. Do not connect COM, NO, or NC to any load.", fill=NAVY, font=font(25))

# Nano
d.rounded_rectangle((100, 325, 570, 820), radius=24, fill=LIGHT, outline=NAVY, width=5)
d.text((155, 365), "Arduino Nano", fill=NAVY, font=font(38, True))
d.text((155, 425), "USB", fill=BLUE, font=font(25, True))
d.text((155, 468), "D2   button input", fill=NAVY, font=font(26))
d.text((155, 525), "D7   relay output", fill=NAVY, font=font(26))
d.text((155, 582), "5V   relay power", fill=NAVY, font=font(26))
d.text((155, 639), "GND  common", fill=NAVY, font=font(26))
d.text((155, 718), "INPUT_PULLUP on D2", fill=GRAY, font=font(22))
d.text((155, 754), "Relay commanded OFF at startup", fill=GRAY, font=font(22))

# Button
d.rounded_rectangle((1080, 310, 1465, 475), radius=22, fill="white", outline=NAVY, width=5)
d.text((1150, 345), "Momentary button", fill=NAVY, font=font(29, True))
d.text((1150, 400), "Normally open", fill=GRAY, font=font(24))

# Relay module
d.rounded_rectangle((980, 555, 1490, 870), radius=24, fill=LIGHT, outline=NAVY, width=5)
d.text((1045, 590), "5 V relay module", fill=NAVY, font=font(34, True))
d.text((1045, 655), "IN", fill=NAVY, font=font(27, True))
d.text((1045, 705), "VCC", fill=NAVY, font=font(27, True))
d.text((1045, 755), "GND", fill=NAVY, font=font(27, True))
d.text((1260, 655), "COM / NO / NC", fill=RED, font=font(25, True))
d.text((1260, 704), "NOT CONNECTED", fill=RED, font=font(24, True))
d.text((1260, 752), "during bench test", fill=RED, font=font(22))

# Connections with labels
def line(points, color, width=8):
    d.line(points, fill=color, width=width, joint="curve")

line([(570, 480), (865, 480), (865, 370), (1080, 370)], BLUE)
d.text((650, 438), "D2", fill=BLUE, font=font(23, True))
line([(1080, 430), (915, 430), (915, 790), (570, 790)], NAVY)
d.text((795, 746), "GND", fill=NAVY, font=font(23, True))

line([(570, 535), (770, 535), (770, 675), (980, 675)], GREEN)
d.text((655, 495), "D7 → IN", fill=GREEN, font=font(23, True))
line([(570, 595), (735, 595), (735, 725), (980, 725)], RED)
d.text((610, 558), "5V → VCC", fill=RED, font=font(23, True))
line([(570, 655), (690, 655), (690, 775), (980, 775)], NAVY)
d.text((590, 620), "GND", fill=NAVY, font=font(23, True))

d.text((70, 920), "Firmware: firmware/benchy_relay_test/benchy_relay_test.ino", fill=GRAY, font=font(22))
d.text((1015, 920), "Copyright © 2026 Erdene Batbayar", fill=GRAY, font=font(22))

PNG.parent.mkdir(parents=True, exist_ok=True)
img.save(PNG, quality=95)

SVG.write_text(
    f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
<rect width="1600" height="1000" fill="white"/>
<style>.t{{font-family:Arial,sans-serif;fill:{NAVY}}}.h{{font-weight:700}}.s{{font-size:24px}}.m{{font-size:27px}}.l{{font-size:42px}}</style>
<text class="t h l" x="70" y="82">Benchy — Kira 03 • Arduino Nano + Relay Bench Test</text>
<text class="t s" x="70" y="125" fill="{GRAY}">Reference low-energy connection • Relay contacts remain disconnected</text>
<rect x="70" y="150" width="1460" height="95" rx="18" fill="{YELLOW}" stroke="#C78A00" stroke-width="4"/>
<text class="t h s" x="95" y="197">SCOPE</text><text class="t s" x="205" y="197">Use only with a verified 5 V logic-compatible relay module.</text>
<text class="t s" x="205" y="230">Power the Nano by USB for this test. Do not connect COM, NO, or NC to any load.</text>
<rect x="100" y="325" width="470" height="495" rx="24" fill="{LIGHT}" stroke="{NAVY}" stroke-width="5"/>
<text class="t h" x="155" y="405" font-size="38">Arduino Nano</text><text class="t h s" x="155" y="455" fill="{BLUE}">USB</text>
<text class="t m" x="155" y="495">D2   button input</text><text class="t m" x="155" y="552">D7   relay output</text><text class="t m" x="155" y="609">5V   relay power</text><text class="t m" x="155" y="666">GND  common</text>
<text class="t s" x="155" y="748" fill="{GRAY}">INPUT_PULLUP on D2</text><text class="t s" x="155" y="784" fill="{GRAY}">Relay commanded OFF at startup</text>
<rect x="1080" y="310" width="385" height="165" rx="22" fill="white" stroke="{NAVY}" stroke-width="5"/><text class="t h m" x="1150" y="385">Momentary button</text><text class="t s" x="1150" y="435" fill="{GRAY}">Normally open</text>
<rect x="980" y="555" width="510" height="315" rx="24" fill="{LIGHT}" stroke="{NAVY}" stroke-width="5"/><text class="t h" x="1045" y="630" font-size="34">5 V relay module</text><text class="t h m" x="1045" y="682">IN</text><text class="t h m" x="1045" y="732">VCC</text><text class="t h m" x="1045" y="782">GND</text><text class="h m" x="1260" y="682" fill="{RED}" font-family="Arial">COM / NO / NC</text><text class="h s" x="1260" y="728" fill="{RED}" font-family="Arial">NOT CONNECTED</text><text class="s" x="1260" y="770" fill="{RED}" font-family="Arial">during bench test</text>
<path d="M570 480 H865 V370 H1080" fill="none" stroke="{BLUE}" stroke-width="8"/><text class="h s" x="650" y="462" fill="{BLUE}" font-family="Arial">D2</text>
<path d="M1080 430 H915 V790 H570" fill="none" stroke="{NAVY}" stroke-width="8"/><text class="h s" x="795" y="772" fill="{NAVY}" font-family="Arial">GND</text>
<path d="M570 535 H770 V675 H980" fill="none" stroke="{GREEN}" stroke-width="8"/><text class="h s" x="655" y="522" fill="{GREEN}" font-family="Arial">D7 → IN</text>
<path d="M570 595 H735 V725 H980" fill="none" stroke="{RED}" stroke-width="8"/><text class="h s" x="610" y="582" fill="{RED}" font-family="Arial">5V → VCC</text>
<path d="M570 655 H690 V775 H980" fill="none" stroke="{NAVY}" stroke-width="8"/><text class="h s" x="590" y="642" fill="{NAVY}" font-family="Arial">GND</text>
<text class="s" x="70" y="950" fill="{GRAY}" font-family="Arial">Firmware: firmware/benchy_relay_test/benchy_relay_test.ino</text><text class="s" x="1015" y="950" fill="{GRAY}" font-family="Arial">Copyright © 2026 Erdene Batbayar</text>
</svg>''',
    encoding="utf-8",
)

print(PNG)
print(SVG)
