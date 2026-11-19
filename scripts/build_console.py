"""Generate GitHub-compatible self-contained console images from the latest snake."""
from base64 import b64encode
from pathlib import Path
from xml.etree import ElementTree as ET

from screen import screen

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
DISPLAY = (387, 96, 1247, 576)


def compose(body_data, source, compact, still):
    # Both crops keep the physical controls visible. On phones the screen wraps
    # the 53-week grid across two rows so that the snake remains recognizable.
    viewport = "62 9 1897 760" if compact else "0 0 2021 778"
    oled = screen(*DISPLAY, compact=compact, source=source, still=still)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
        viewBox="{viewport}" role="img" aria-labelledby="device-title device-description">
<title id="device-title">Dong 的贡献掌机</title>
<desc id="device-description">钛灰色掌机的 OLED 屏幕自动回放真实公开贡献。蛇每吃掉一个有贡献的日期，屏幕上的日期计数增加。</desc>
<image x="0" y="0" width="2021" height="778" xlink:href="data:image/webp;base64,{body_data}"/>
{oled}
</svg>'''


def main():
    body_data = b64encode((ASSETS / "handheld-body.webp").read_bytes()).decode("ascii")
    source = ASSETS / "contribution-snake-dark.svg"
    results = {}
    for compact, prefix in ((False, "console"), (True, "console-mobile")):
        for still, suffix in ((False, ""), (True, "-still")):
            results[f"{prefix}{suffix}.svg"] = compose(body_data, source, compact, still)
    for value in results.values():
        ET.fromstring(value)
    for name, value in results.items():
        (ASSETS / name).write_text(value, encoding="utf-8")


if __name__ == "__main__":
    main()
