"""Stable paragraph ids added at response time (stored HTML is untouched).

Every <p>, <li>, <tr>, <dd> and heading inside <body> gets id="<prefix>-N" in document order.
The same function is used offline to build the paragraph index, so ids always agree.
"""
import re

_BLOCK = re.compile(r'<(p|li|tr|dd|h[1-6])\b([^>]*)>', re.I)
CSS = ('<style>[id^="lp-"],[id^="gp-"]{scroll-margin-top:84px}'
       '.rd-hit{background:#ffe4ef!important;box-shadow:0 0 0 3px #f9a8c9;border-radius:4px;transition:background 1.5s}'
       'tr.rd-hit td{background:#ffe4ef!important}</style>')
JS = ('<script>(function(){var h=location.hash.slice(1);if(!/^(lp|gp)-\\d+$/.test(h))return;'
      'function go(){var e=document.getElementById(h)||document.querySelector("[data-pid=\\""+h+"\\"]");if(!e)return;e.classList.add("rd-hit");'
      'e.scrollIntoView({block:"center"});}'
      'if(document.readyState!="loading")go();else document.addEventListener("DOMContentLoaded",go);'
      'setTimeout(go,400);})();</script>')


def add_ids(html, prefix):
    m = re.search(r'<body\b[^>]*>', html, re.I)
    start = m.end() if m else 0
    counter = [0]

    def sub(mt):
        i = counter[0]; counter[0] += 1
        if re.search(r'\bid\s*=', mt.group(2), re.I):
            return f'<a id="{prefix}-{i}"></a>' + mt.group(0) if mt.group(1).lower() not in ('tr', 'li') else mt.group(0)[:-1] + f' data-pid="{prefix}-{i}">'
        return f'<{mt.group(1)}{mt.group(2)} id="{prefix}-{i}">'
    body = _BLOCK.sub(sub, html[start:])
    return html[:start] + body


def decorate(html):
    html = re.sub(r'</head>', lambda m: CSS + m.group(0), html, count=1, flags=re.I)
    return re.sub(r'</body>', lambda m: JS + m.group(0), html, count=1, flags=re.I)


def paragraphs(html, prefix):
    """[(id, text)] for indexing; text is tag-stripped, whitespace-collapsed."""
    out = []
    tagged = add_ids(html, prefix)
    for mt in re.finditer(r'<(p|li|tr|dd|h[1-6])\b[^>]*\bid="(%s-\d+)"[^>]*>(.*?)</\1>' % prefix, tagged, re.I | re.S):
        t = re.sub(r'<[^>]+>', ' ', mt.group(3))
        t = re.sub(r'&nbsp;', ' ', t); t = re.sub(r'\s+', ' ', t).strip()
        if len(t) >= 25:
            out.append((mt.group(2), mt.group(1).lower(), t))
    return out
