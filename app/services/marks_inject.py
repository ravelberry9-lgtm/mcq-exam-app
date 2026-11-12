"""Add the highlight / bookmark tools to every HTML page the app serves (shared layouts and raw note files)."""
from flask import request, url_for
from .csrf import csrf_token

SKIP = ('/admin', '/access', '/account', '/static/')


def init_marks_inject(app):
    @app.after_request
    def _inject(resp):
        try:
            if resp.status_code != 200 or not (resp.mimetype or '').startswith('text/html') or resp.is_streamed and not resp.direct_passthrough:
                return resp
            if resp.direct_passthrough:            # send_file(): read the file so we can add the tools
                resp.direct_passthrough = False
            p = request.path
            if p.endswith('/content'):              # raw files shown inside a reader frame must stay byte-exact
                return resp
            if any(p == s.rstrip('/') or p.startswith(s if s.endswith('/') else s + '/') for s in SKIP):
                return resp
            body = resp.get_data(as_text=True)
            if '</body>' not in body or 'study_tools.js' in body and 'data-mk-auto' in body:
                return resp
            add = ''
            if 'name="csrf-token"' not in body:
                add += '<meta name="csrf-token" content="%s">' % csrf_token()
            if 'study_tools.css' not in body:
                add += '<link rel="stylesheet" href="%s">' % url_for('static', filename='study_tools.css', v='st4')
            if 'study_tools.js' not in body:
                add += '<script src="%s" defer></script>' % url_for('static', filename='study_tools.js', v='st4')
            add += '<script data-mk-auto>window.MK_SAVED=%r;window.MK_ACCOUNT=%r;</script>' % (url_for('polity_marks.saved'), url_for('account.home'))
            i = body.rfind('</body>')
            resp.set_data(body[:i] + add + body[i:])
        except Exception:
            pass
        return resp
