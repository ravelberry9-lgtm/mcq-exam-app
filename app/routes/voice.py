"""Issues a short-lived signed token so the voice service knows which device is calling."""
from flask import Blueprint, current_app, g, jsonify, render_template, request
from itsdangerous import URLSafeTimedSerializer

bp = Blueprint("voice", __name__)


@bp.route("/voice/token", methods=["GET", "POST"])
def voice_token():
    dev = getattr(g, "device_id", None) or request.cookies.get("device_id")
    if not dev or dev == "anon":
        return jsonify(error="no device"), 400
    tok = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt="voice-device-v1").dumps({"d": dev})
    resp = jsonify(token=tok, expires_in=3600)
    resp.headers["Cache-Control"] = "no-store"
    return resp


@bp.route("/voice")
def voice_page():
    origin = (current_app.config.get("VOICE_SERVICE_ORIGIN") or __import__("os").environ.get("VOICE_SERVICE_ORIGIN") or "").rstrip("/")
    return render_template("voice.html", voice_origin=origin)


@bp.route("/voice/live")
def voice_live():
    origin = (current_app.config.get("VOICE_SERVICE_ORIGIN") or __import__("os").environ.get("VOICE_SERVICE_ORIGIN") or "").rstrip("/")
    return render_template("voice_live.html", voice_origin=origin)
