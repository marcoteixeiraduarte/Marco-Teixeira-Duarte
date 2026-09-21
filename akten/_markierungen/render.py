#!/usr/bin/env python3
"""FamilySearch-ähnliche Markierungen auf die Akten-Scans legen."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from felder import FELDER, KIND_FARBE, KIND_ALPHA  # noqa: E402

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
AKTEN = ROOT / "akten"


def signature_for(name: str) -> str | None:
    n = name.replace("-markiert", "")
    hits = [key for key in FELDER if key in n]
    if not hits:
        return None
    return max(hits, key=len)


def rel_box(im: Image.Image, box: list[float]) -> tuple[int, int, int, int]:
    w, h = im.size
    x = int(box[0] * w)
    y = int(box[1] * h)
    bw = max(8, int(box[2] * w))
    bh = max(8, int(box[3] * h))
    x = max(0, min(x, w - 2))
    y = max(0, min(y, h - 2))
    bw = min(bw, w - x)
    bh = min(bh, h - y)
    return x, y, bw, bh


def font_for(h: int) -> ImageFont.FreeTypeFont:
    size = max(14, min(36, h // 45))
    return ImageFont.truetype(FONT_PATH, size)


def render_one(src: Path, dest: Path, felder: list[dict]) -> None:
    im = Image.open(src).convert("RGB")
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay, "RGBA")
    font = font_for(im.size[1])

    for feld in felder:
        x, y, bw, bh = rel_box(im, feld["box"])
        rgb = KIND_FARBE[feld["kind"]]
        a = KIND_ALPHA.get(feld["kind"], 80)
        draw.rounded_rectangle(
            [x, y, x + bw, y + bh],
            radius=min(14, bh // 6, bw // 6),
            fill=(*rgb, a),
            outline=(*rgb, min(255, a + 90)),
            width=max(2, im.size[1] // 500),
        )
        label = feld.get("label") or ""
        if not label:
            continue
        # Chip oben links in der Fläche, Schrift bleibt lesbar.
        tb = draw.textbbox((0, 0), label, font=font)
        tw, th = tb[2] - tb[0] + 10, tb[3] - tb[1] + 6
        cx, cy = x + 4, max(2, y - th - 2) if y > th + 4 else y + 4
        if cx + tw > im.size[0] - 4:
            cx = max(2, im.size[0] - tw - 4)
        draw.rounded_rectangle(
            [cx, cy, cx + tw, cy + th],
            radius=4,
            fill=(25, 25, 25, 210),
        )
        draw.text((cx + 5, cy + 2), label, font=font, fill=(255, 255, 255, 255))

    out = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")
    dest.parent.mkdir(parents=True, exist_ok=True)
    out.save(dest, quality=85, optimize=True)


def marked_name(path: Path) -> Path:
    return path.with_name(path.stem + "-markiert.jpg")


def patch_readme(readme: Path) -> bool:
    text = readme.read_text(encoding="utf-8")
    if "-markiert.jpg" in text:
        return False
    folder = readme.parent
    marked = sorted(folder.glob("*-markiert.jpg"))
    if not marked:
        return False

    legend = (
        "Markierung wie bei FamilySearch: **farbige Flächen = Fundstellen** "
        "(nicht die ganze Seite). Darunter der unveränderte Scan zur Gegenlese.\n\n"
        "🟨 Name · 🟧 Datum · 🟦 Ort · 🟩 Eltern · 🟪 Avós · "
        "🟥 Randvermerk · 🩵 Paten (nicht Elternort)\n"
    )
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    inserted_legend = False
    while i < len(lines):
        line = lines[i]
        if line.strip() == "## Scan" and not inserted_legend:
            out.append(line)
            out.append("")
            out.append(legend.rstrip())
            out.append("")
            inserted_legend = True
            i += 1
            # skip the old intro sentence if present
            if i < len(lines) and lines[i].strip() == "":
                i += 1
            if i < len(lines) and "Gegenlesen" in lines[i]:
                i += 1
            if i < len(lines) and lines[i].strip() == "":
                i += 1
            continue
        # prepend marked image before an unmarked local jpg embed
        if line.startswith("![") and "](" in line and line.endswith(")"):
            inner = line[line.index("](") + 2 : -1]
            if (
                inner.endswith(".jpg")
                and not inner.startswith("http")
                and "../" not in inner
                and "-markiert" not in inner
            ):
                mpath = folder / inner
                marked_file = marked_name(mpath)
                if marked_file.exists():
                    alt = line[2 : line.index("]")]
                    out.append(f"![{alt} — Fundstellen]({marked_file.name})")
                    out.append("")
                    out.append(f"<details><summary>Scan ohne Markierung — {alt}</summary>")
                    out.append("")
                    out.append(line)
                    out.append("")
                    out.append("</details>")
                    out.append("")
                    i += 1
                    continue
        out.append(line)
        i += 1
    new = "\n".join(out).rstrip() + "\n"
    if new != text:
        readme.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    only = {a for a in sys.argv[1:] if not a.startswith("-")}
    cache: dict[str, Path] = {}
    rendered = 0
    copied = 0
    jpgs = [
        p
        for p in AKTEN.rglob("*.jpg")
        if "-markiert" not in p.name and p.parent.name != "_markierungen"
    ]
    # render unique signatures first
    for p in jpgs:
        key = signature_for(p.name)
        if not key:
            continue
        if only and key not in only:
            continue
        dest = marked_name(p)
        if key not in cache:
            render_one(p, dest, FELDER[key])
            cache[key] = dest
            rendered += 1
        elif dest.resolve() != cache[key].resolve():
            shutil.copy2(cache[key], dest)
            copied += 1
        print(f"  {dest.relative_to(ROOT)}")

    patched = 0
    for readme in AKTEN.rglob("README.md"):
        if patch_readme(readme):
            patched += 1
            print(f"README {readme.relative_to(ROOT)}")

    print(f"rendered={rendered} copied={copied} readmes={patched}")


if __name__ == "__main__":
    main()
