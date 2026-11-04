"""Issues a short-lived signed token so the voice service knows which device is calling."""
from flask import Blueprint, current_app, jsonify, render_template, request
from itsdangerous import URLSafeTimedSerializer

bp = Blueprint("voice", __name__)


@bp.route("/voice/token", methods=["POST"])
def voice_token():
    dev = request.cookies.get("device_id")
    if not dev or dev == "anon":
        return jsonify(error="no device"), 400
    tok = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt="voice-device-v1").dumps({"d": dev})
    return jsonify(token=tok, expires_in=3600)


@bp.route("/voice")
def voice_page():
    origin = (current_app.config.get("VOICE_SERVICE_ORIGIN") or __import__("os").environ.get("VOICE_SERVICE_ORIGIN") or "").rstrip("/")
    return render_template("voice.html", voice_origin=origin)
