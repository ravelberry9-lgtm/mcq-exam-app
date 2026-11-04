"""Short-lived device token issued by the Flask app, verified here. Same SECRET_KEY, same salt."""
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

SALT = "voice-device-v1"


def make_token(secret: str, device_id: str) -> str:
    return URLSafeTimedSerializer(secret, salt=SALT).dumps({"d": device_id})


def verify_token(secret: str, token: str, max_age: int = 3600) -> str | None:
    try:
        return URLSafeTimedSerializer(secret, salt=SALT).loads(token, max_age=max_age)["d"]
    except (BadSignature, SignatureExpired, KeyError):
        return None
