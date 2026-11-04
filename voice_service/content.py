"""Notes search over the app's own content.

Telugu is agglutinative (శాతవాహనుల / శాతవాహనులు / శాతవాహనులకు), so exact word match misses
many hits. Each word is therefore indexed both whole and as character n-grams, and scored with BM25.
Everything stays in memory: the whole AP History notes set is only a few MB of text.
"""
import html
import math
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass

REF = re.compile(r"\[RR:[^\]]*\]")  # internal source markers such as [RR: RR5-F030]; never shown or spoken
TAG = re.compile(r"<[^>]+>")
BLOCK_END = re.compile(r"</(p|li|h[1-6]|tr|div|ul|ol|table)>|<br\s*/?>", re.I)
WORD = re.compile(r"[ఀ-౿]+|[a-z]+|\d+")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s or "").lower()
    return s.replace("‌", "").replace("‍", "")


_FOLD = str.maketrans({
    "శ": "స", "ష": "స",
    "ఖ": "గ", "ఘ": "గ", "క": "గ", "ఛ": "జ", "ఝ": "జ", "చ": "జ", "ఠ": "డ", "ఢ": "డ", "ట": "డ",
    "థ": "ద", "ధ": "ద", "త": "ద", "ఫ": "బ", "భ": "బ", "ప": "బ",
    "ఆ": "అ", "ఈ": "ఇ", "ఊ": "ఉ", "ఏ": "ఎ", "ఓ": "ఒ", "ఐ": "ఎ", "ఔ": "ఒ",
    "ా": "", "ీ": "ి", "ూ": "ు", "ే": "ె", "ో": "ొ", "ై": "ె", "ౌ": "ొ",
    "ఁ": "ం", "ః": "",
})


def fold(w: str) -> str:
    """Sound-alike form of a Telugu word. Speech recognizers confuse శ/స, త/ద, క/గ and long/short vowels, so the
    search compares words after this folding. Only used for search features, never shown."""
    return w.translate(_FOLD)


def words(s: str) -> list[str]:
    return WORD.findall(norm(s))


def html_to_paragraphs(h: str) -> list[str]:
    h = REF.sub(" ", h or "")
    h = BLOCK_END.sub("\n", h)
    h = html.unescape(TAG.sub(" ", h))
    out = []
    for line in h.split("\n"):
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            out.append(line)
    return out


@dataclass
class Chunk:
    id: int
    subject: str
    chapter_id: int
    chapter_num: int
    chapter_title_te: str
    chapter_title_en: str
    section_num: int
    heading: str
    text: str


def make_chunks(rows, min_chars=350, max_chars=900) -> list[Chunk]:
    chunks, cid = [], 0
    for r in rows:
        paras = html_to_paragraphs(r["body_te"])
        buf = ""
        def flush():
            nonlocal buf, cid
            if buf.strip():
                chunks.append(Chunk(cid, r["slug"], r["chapter_id"], r["chapter_num"], r["title_te"] or "",
                                    r["title_en"] or "", r["section_num"], r["heading_te"] or "", buf.strip()))
                cid += 1
            buf = ""
        for p in paras:
            if buf and len(buf) + len(p) > max_chars:
                flush()
            buf = (buf + " " + p).strip()
            if len(buf) >= min_chars:
                flush()
        flush()
    return chunks


def load_note_rows(engine):
    from sqlalchemy import text
    q = text("""
        SELECT n.id AS note_id, n.chapter_id, n.section_num, n.heading_te, n.body_te,
               c.chapter_num, c.title_te, c.title_en, s.slug
        FROM notes n JOIN chapters c ON c.id = n.chapter_id JOIN subjects s ON s.id = c.subject_id
        ORDER BY s.slug, c.chapter_num, n.section_num""")
    with engine.connect() as conn:
        return [dict(r._mapping) for r in conn.execute(q)]


def features(word: str, n: int):
    if word.isdigit():
        return ["#" + word]
    if word.isascii():
        return ["l:" + word]
    feats = ["w:" + word]
    padded = "^" + word + "$"
    if len(padded) <= n:
        return feats + ["g:" + padded]
    return feats + ["g:" + padded[i:i + n] for i in range(len(padded) - n + 1)]


class NotesIndex:
    def __init__(self, chunks: list[Chunk], ngram: int = 3, k1: float = 1.2, b: float = 0.75):
        self.chunks, self.n, self.k1, self.b = chunks, ngram, k1, b
        self.inv: dict[str, list[tuple[int, int]]] = defaultdict(list)
        self.len = []
        for i, c in enumerate(chunks):
            cnt = Counter(f for w in words(c.heading + " " + c.text) for f in features(fold(w), ngram))
            self.len.append(sum(cnt.values()))
            for f, t in cnt.items():
                self.inv[f].append((i, t))
        self.avg = (sum(self.len) / len(self.len)) if self.len else 1.0
        self.N = len(chunks)

    def search(self, query: str, k: int = 4, subject: str | None = None, chapter_id: int | None = None):
        qf = Counter(f for w in words(query) for f in features(fold(w), self.n))
        scores: dict[int, float] = defaultdict(float)
        for f, qt in qf.items():
            post = self.inv.get(f)
            if not post:
                continue
            idf = math.log(1 + (self.N - len(post) + 0.5) / (len(post) + 0.5))
            for i, t in post:
                norm_len = 1 - self.b + self.b * self.len[i] / self.avg
                scores[i] += idf * (t * (self.k1 + 1)) / (t + self.k1 * norm_len)
        ranked = sorted(scores.items(), key=lambda x: -x[1])
        out = []
        for i, s in ranked:
            c = self.chunks[i]
            if subject and c.subject != subject:
                continue
            if chapter_id and c.chapter_id != chapter_id:
                continue
            out.append((c, round(s, 2)))
            if len(out) == k:
                break
        return out
