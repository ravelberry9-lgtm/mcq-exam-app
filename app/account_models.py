"""Learner accounts: a username + password that maps to one shared device id, so progress, bookmarks and
highlights follow the learner across phone and tablet."""
from datetime import datetime
from .db import db


class LearnerAccount(db.Model):
    __tablename__ = 'learner_account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), unique=True, nullable=False, index=True)
    pw_hash = db.Column(db.String(255), nullable=False)
    recovery_hash = db.Column(db.String(255), nullable=False)
    device_id = db.Column(db.String(64), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_login_at = db.Column(db.DateTime)


class AppSetting(db.Model):
    """Small key/value settings changed from the admin panel (e.g. the hashed app access code)."""
    __tablename__ = 'app_setting'
    key = db.Column(db.String(64), primary_key=True)
    value = db.Column(db.String(500), nullable=False, default='')
