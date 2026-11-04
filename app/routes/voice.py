"""Issues a short-lived signed token so the voice service knows which device is calling."""
from flask import Blueprint, current_app, jsonify, request
from itsdangerous import URLSafeTimedSerializer

bp = Blueprint("voice", __name__)


@bp.route("/voice/token", methods=["POST"])
def voice_token():
    dev = request.cookies.get("device_id")
    if not dev or dev == "anon":
        return jsonify(error="no device"), 400
    tok = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt="voice-device-v1").dumps({"d": dev})
    return jsonify(token=tok, expires_in=3600)
