"""Images inside stored notes.

Notes imported from the AP History HTML carry bare relative ``src`` values (``ap_ch06_ikshvaku_sites.jpg``). On a Learn
page that resolves to ``/learn/topic/<id>/<file>`` and 404s. This module fixes that at render time, without touching the
stored notes:

* a relative ``src`` is looked up under ``static/notes``: first as that exact relative path, then by a *unique* path-suffix
  match among the shipped image files (so ``wiki_images/x.jpg`` finds ``AP_History/Chapters/wiki_images/x.jpg``);
  a match becomes the absolute application path ``/static/notes/...``;
* ``/static/...`` paths are kept only if the file exists;
* ``http(s)`` images are left alone (they cannot be checked here);
* anything else, including an ``<img>`` whose ``src`` the sanitiser removed, is replaced by a visible
  "Image unavailable - source needed" notice that names the file, never by a broken-image icon.
"""
import html as _html
import os
import re
from functools import lru_cache
from pathlib import PurePosixPath
from urllib.parse import unquote

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "static")
NOTES_ROOT = os.path.join(STATIC_ROOT, "notes")
IMAGE_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg")

_IMG = re.compile(r"<img\b[^>]*>", re.I)
_ATTR = re.compile(r'([a-zA-Z_:][-\w:.]*)\s*=\s*"([^"]*)"')


@lru_cache(maxsize=1)
def _index():
    """({relative path under static/notes}, {path suffix -> [relative paths]}) for every shipped image file."""
    files, suffixes = set(), {}
    for dirpath, _dirs, names in os.walk(NOTES_ROOT):
        for name in names:
            if not name.lower().endswith(IMAGE_EXT):
                continue
            rel = PurePosixPath(os.path.relpath(os.path.join(dirpath, name), NOTES_ROOT).replace(os.sep, "/"))
            files.add(str(rel))
            parts = rel.parts
            for i in range(len(parts)):
                suffixes.setdefault("/".join(parts[i:]), []).append(str(rel))
    return files, suffixes


def refresh():
    """Forget the cached file index (tests, or after assets are added while the process runs)."""
    _index.cache_clear()


def _clean_rel(src):
    parts = [p for p in unquote(src).replace("\\", "/").split("/") if p not in ("", ".")]
    if any(p == ".." for p in parts) or not parts:
        return None
    return "/".join(parts)


def resolve(src):
    """Return ``(url, kind)``: kind is 'external', 'local' or 'missing' (url None)."""
    s = (src or "").strip()
    if not s:
        return None, "missing"
    low = s.lower()
    if low.startswith(("http://", "https://")):
        return s, "external"
    if s.startswith("//") or ":" in s.split("/")[0]:
        return None, "missing"                                      # protocol-relative, data:, javascript:, file: ...
    files, suffixes = _index()
    if s.startswith("/"):
        if s.startswith("/static/"):
            rel = _clean_rel(s[len("/static/"):])
            if rel and os.path.isfile(os.path.join(STATIC_ROOT, *rel.split("/"))):
                return "/static/" + rel, "local"
        return None, "missing"
    rel = _clean_rel(s)
    if rel is None:
        return None, "missing"
    if rel in files:
        return "/static/notes/" + rel, "local"
    hits = suffixes.get(rel, [])
    if len(hits) == 1:
        return "/static/notes/" + hits[0], "local"
    return None, "missing"                                          # unknown, or ambiguous: never guess


def _notice(name):
    label = _html.escape(os.path.basename(unquote(name or "").replace("\\", "/")) or "image")
    return ('<span class="note-img-missing" role="note">Image unavailable &middot; చిత్రం అందుబాటులో లేదు '
            f'&mdash; source needed: <code>{label}</code></span>')


def rewrite_images(cleaned_html):
    """Apply the rules above to already-sanitised note HTML."""
    def one(m):
        attrs = dict((k.lower(), v) for k, v in _ATTR.findall(m.group(0)))
        raw = _html.unescape(attrs.get("src", ""))
        url, kind = resolve(raw)
        if kind == "missing":
            return _notice(raw)
        out = [f'src="{_html.escape(url, quote=True)}"', f'alt="{attrs.get("alt", "")}"', 'loading="lazy"']
        for k in ("width", "height"):
            if k in attrs:
                out.append(f'{k}="{attrs[k]}"')
        return "<img " + " ".join(out) + ">"
    return _IMG.sub(one, cleaned_html or "")
