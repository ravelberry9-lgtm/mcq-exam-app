"""Build the deployable Raghunatha Rao scan/text library for AP History.

The audit workspace keeps archival JPEGs and original spread scans.  The app
ships only one optimised facsimile for each printed page, its manually verified
Telugu text, a manifest, and small Telugu viewers.  No OCR is performed here.
"""
from __future__ import annotations

import argparse
import html
import json
import shutil
from pathlib import Path

from PIL import Image


CHAPTERS = {
    15: ("ch02_03", 31, 47, "RR అధ్యాయం 2 — యూరోపియన్ వర్తక సంస్థలు"),
    16: ("ch02_03", 48, 68, "RR అధ్యాయం 3 — నిజాం ప్రభుత్వం, ఈస్ట్ ఇండియా కంపెనీ"),
    17: ("ch04_05", 69, 90, "RR అధ్యాయం 4 — కంపెనీ పాలనలో ఆంధ్రదేశం"),
    18: ("ch04_05", 91, 105, "RR అధ్యాయం 5 — బ్రిటిషు పాలనలో ఆంధ్రదేశం"),
    19: ("ch06", 106, 117, "RR అధ్యాయం 6 — హైదరాబాద్ రాష్ట్రం, 1857–1911"),
    20: ("ch07_08", 118, 133, "RR అధ్యాయం 7 — ఆంధ్రదేశంలో ప్రజాచైతన్యం"),
    21: ("ch07_08", 134, 156, "RR అధ్యాయం 8 — ఆంధ్రోద్యమ ఆవిర్భావం"),
    22: ("ch09_10", 157, 182, "RR అధ్యాయం 9 — ఆంధ్రలో భారత జాతీయోద్యమం"),
    23: ("ch09_10", 183, 195, "RR అధ్యాయం 10 — మద్రాసు రాజకీయాల్లో ఆంధ్రులు"),
    24: ("ch11_13", 196, 201, "RR అధ్యాయం 11 — తెలంగాణలో రాజకీయ చైతన్యం"),
    25: ("ch11_13", 202, 215, "RR అధ్యాయం 12 — తెలంగాణలో స్వాతంత్ర్యోద్యమం"),
    26: ("ch11_13", 216, 224, "RR అధ్యాయం 13 — హైదరాబాద్‌పై పోలీసు చర్య"),
    27: ("ch14_15", 225, 242, "RR అధ్యాయం 14 — ఆంధ్ర రాష్ట్ర అవతరణ"),
    28: ("ch14_15", 243, 257, "RR అధ్యాయం 15 — ఆంధ్రప్రదేశ్ అవతరణ"),
    29: ("ch16_17", 258, 279, "RR అధ్యాయం 16 — కమ్యూనిస్టు పార్టీలు, సాయుధ పోరాటాలు"),
    30: ("ch16_17", 280, 291, "RR అధ్యాయం 17 — 1956 తరువాత రాజకీయ సంక్షోభాలు"),
    31: ("ch18_23", 292, 300, "RR అధ్యాయం 18 — ఎన్టీఆర్ ప్రభుత్వం తొలగింపు"),
    32: ("ch18_23", 301, 305, "RR అధ్యాయం 19 — ఎన్టీఆర్ మూడవ మంత్రివర్గం"),
    33: ("ch18_23", 306, 309, "RR అధ్యాయం 20 — పి.వి. నరసింహారావు"),
    34: ("ch18_23", 310, 315, "RR అధ్యాయం 21 — తెలుగుదేశం పార్టీలో చీలిక"),
    35: ("ch18_23", 316, 318, "RR అధ్యాయం 22 — చంద్రబాబు నాయుడు ప్రభుత్వం"),
    36: ("ch18_23", 319, 329, "RR అధ్యాయం 23 — పరిపాలనా సంస్కరణలు"),
    37: ("ch24_25", 330, 338, "RR అధ్యాయం 24 — కాంగ్రెస్ పునరుజ్జీవనం"),
    38: ("ch24_25", 339, 351, "RR అధ్యాయం 25 — 2009 సాధారణ ఎన్నికలు"),
    39: (None, None, None, "2009 తరువాతి విభజన — RR ఆధార అధ్యాయం లేదు"),
    40: ("appendix_1", 353, 399, "RR అనుబంధం I — తెలుగు సాహిత్య చారిత్రక సర్వేక్షణ"),
    41: ("appendix_2", 400, 403, "RR అనుబంధం II — ప్రముఖ ఆంధ్ర వ్యక్తులు"),
}


def _viewer(title: str, pages: list[dict]) -> str:
    nav = "".join(f'<a href="#page-{p["printed_page"]:03d}">{p["printed_page"]}</a>' for p in pages)
    cards = []
    for page in pages:
        number = page["printed_page"]
        text = html.escape(page["text_value"])
        cards.append(
            f'<article id="page-{number:03d}"><h2>ముద్రిత పుట {number}</h2>'
            f'<p class="status">scanతో మాన్యువల్‌గా ధృవీకరించిన పాఠ్యం</p>'
            f'<div class="scan"><img src="printed_pages/printed_{number:03d}.webp" '
            f'loading="lazy" alt="RR ముద్రిత పుట {number}"></div>'
            f'<div class="text"><pre>{text}</pre></div></article>'
        )
    return f'''<!doctype html><html lang="te"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>
body{{margin:0;background:#eee8dd;color:#211b16;font-family:"Noto Sans Telugu","Nirmala UI",sans-serif;line-height:1.7}}header,nav,main{{max-width:1100px;margin:auto}}header{{padding:20px 14px}}h1,h2{{color:#174f5f}}.rule{{background:#fff4ce;border-left:5px solid #d49308;padding:11px 14px}}.controls{{display:flex;gap:10px}}button{{padding:10px 15px;border:1px solid #174f5f;border-radius:9px;background:#fff;color:#174f5f;font:inherit;font-weight:700}}button.on{{background:#174f5f;color:#fff}}nav{{position:sticky;top:0;z-index:2;display:flex;gap:7px;overflow-x:auto;background:#174f5f;padding:8px}}nav a{{color:#fff;text-decoration:none;background:#286b7c;padding:6px 9px;border-radius:6px}}main{{padding:14px}}article{{background:#fff;border:1px solid #d7cbbb;border-radius:12px;padding:14px;margin-bottom:18px}}img{{display:block;width:100%;height:auto}}.text{{display:none}}body.text-mode .scan{{display:none}}body.text-mode .text{{display:block}}pre{{white-space:pre-wrap;font:1rem/1.9 "Noto Sans Telugu","Nirmala UI",sans-serif}}.status{{color:#356b3f}}@media(max-width:620px){{header,main{{padding:8px}}article{{padding:7px}}}}
</style></head><body><header><h1>{html.escape(title)}</h1><p class="rule">ప్రతి cardలో ఒక ముద్రిత పుట మాత్రమే ఉంది. పుట చిత్రం authoritative source; పాఠ్యం దానితో మాన్యువల్‌గా సరిపోల్చబడింది.</p><div class="controls"><button id="scan" class="on">ముద్రిత పుటలు</button><button id="text">పాఠ్యం</button></div></header><nav>{nav}</nav><main>{''.join(cards)}</main><script>const s=document.getElementById('scan'),t=document.getElementById('text');s.onclick=()=>{{document.body.classList.remove('text-mode');s.classList.add('on');t.classList.remove('on')}};t.onclick=()=>{{document.body.classList.add('text-mode');t.classList.add('on');s.classList.remove('on')}};</script></body></html>'''


def build(source: Path, destination: Path, max_side: int, quality: int) -> None:
    manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8"))
    destination.mkdir(parents=True, exist_ok=True)
    output_volumes = []
    for volume in manifest["volumes"]:
        key = volume["key"]
        volume_dir = destination / key
        image_dir = volume_dir / "printed_pages"
        text_dir = volume_dir / "text_pages"
        image_dir.mkdir(parents=True, exist_ok=True)
        text_dir.mkdir(parents=True, exist_ok=True)
        output_pages = []
        for page in volume["printed_pages"]:
            if page.get("text_status") != "manually_verified":
                raise RuntimeError(f'{key} page {page["printed_page"]} is not manually verified')
            number = page["printed_page"]
            source_image = source / page["scan"]
            source_text = source / page["text"]
            target_image = image_dir / f"printed_{number:03d}.webp"
            target_text = text_dir / f"printed_{number:03d}.txt"
            with Image.open(source_image) as image:
                image = image.convert("RGB")
                if max(image.size) > max_side:
                    image.thumbnail((max_side, max_side), Image.Resampling.LANCZOS)
                image.save(target_image, "WEBP", quality=quality, method=6)
            text_value = source_text.read_text(encoding="utf-8").strip()
            target_text.write_text(text_value + "\n", encoding="utf-8")
            output_pages.append({
                "printed_page": number,
                "source_pdf_page": page["source_pdf_page"],
                "scan": f"{key}/printed_pages/{target_image.name}",
                "text": f"{key}/text_pages/{target_text.name}",
                "text_status": "manually_verified",
                "text_value": text_value,
            })
        (volume_dir / "source_pages.html").write_text(_viewer(volume["title_te"], output_pages), encoding="utf-8")
        output_volumes.append({
            "key": key,
            "title_te": volume["title_te"],
            "source_file": volume["source_file"],
            "source_sha256": volume["source_sha256"],
            "first_printed_page": output_pages[0]["printed_page"],
            "last_printed_page": output_pages[-1]["printed_page"],
            "printed_page_count": len(output_pages),
            "missing_printed_pages": volume.get("missing_printed_pages", []),
            "printed_pages": [{k: v for k, v in p.items() if k != "text_value"} for p in output_pages],
            "text_status": "all available printed pages manually verified against scans",
        })
    chapter_map = {
        str(chapter): {
            "volume": volume,
            "first_printed_page": first,
            "last_printed_page": last,
            "title_te": title,
            "viewer": (f"{volume}/source_pages.html#page-{first:03d}" if volume else None),
        }
        for chapter, (volume, first, last, title) in CHAPTERS.items()
    }
    app_manifest = {
        "source": manifest["source"],
        "policy_te": manifest["policy_te"],
        "total_source_pdfs": manifest["total_source_pdfs"],
        "total_scanned_pdf_pages": manifest["total_scanned_pdf_pages"],
        "total_printed_pages": sum(v["printed_page_count"] for v in output_volumes),
        "image_format": f"WebP quality {quality}, maximum side {max_side}px",
        "missing_printed_pages": [352],
        "volumes": output_volumes,
        "app_chapters": chapter_map,
    }
    (destination / "manifest.json").write_text(json.dumps(app_manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (destination / "chapter_map.json").write_text(json.dumps(chapter_map, ensure_ascii=False, indent=2), encoding="utf-8")
    links = "".join(
        f'<article><h2>APP అధ్యాయం {chapter}</h2><p>{html.escape(data[3])}</p>'
        + (f'<a href="{data[0]}/source_pages.html#page-{data[1]:03d}">ముద్రిత పుటలు {data[1]}–{data[2]} / పాఠ్యం</a>' if data[0] else '<p class="rule">ఈ అధ్యాయానికి RR ఆధార పాఠ్యం లేదు.</p>')
        + '</article>'
        for chapter, data in CHAPTERS.items()
    )
    (destination / "index.html").write_text(
        f'''<!doctype html><html lang="te"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>RR తెలుగు మూలగ్రంథం</title><style>body{{margin:0;background:#f4f0e8;color:#251d16;font-family:"Noto Sans Telugu","Nirmala UI",sans-serif;line-height:1.65}}main{{max-width:900px;margin:auto;padding:20px}}header,article{{background:#fff;border:1px solid #dfd4c5;border-radius:12px;padding:16px;margin-bottom:14px}}h1{{color:#773a20}}h2{{color:#174f5f}}a{{display:inline-block;background:#174f5f;color:#fff;text-decoration:none;padding:9px 14px;border-radius:8px}}.rule{{background:#fff4ce;border-left:5px solid #d49308;padding:10px 13px}}</style></head><body><main><header><h1>రఘునాథరావు — తెలుగు మూలగ్రంథం</h1><p>372 లభ్యమైన ముద్రిత పుటలు · scan మరియు verified Telugu text.</p><p class="rule">మూలంలో ముద్రిత పుట 352 లభించలేదు; దానికి text లేదా image కల్పించలేదు.</p></header>{links}</main></body></html>''',
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "static" / "notes" / "AP_History" / "source_facsimiles" / "RR_Telugu",
    )
    parser.add_argument("--max-side", type=int, default=2600)
    parser.add_argument("--quality", type=int, default=82)
    args = parser.parse_args()
    build(args.source.resolve(), args.destination.resolve(), args.max_side, args.quality)


if __name__ == "__main__":
    main()
