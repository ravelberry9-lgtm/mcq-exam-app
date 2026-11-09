"""Additive Unit 6 state; legacy question IDs and learner rows remain intact."""
from datetime import datetime
from .db import db

class PolityUnit6State(db.Model):
    __tablename__='polity_unit6_state'
    device_id=db.Column(db.String(64),primary_key=True)
    item_id=db.Column(db.String(128),primary_key=True)
    saved=db.Column(db.Boolean,nullable=False,default=False)
    seen_count=db.Column(db.Integer,nullable=False,default=0)
    wrong_count=db.Column(db.Integer,nullable=False,default=0)
    last_seen_at=db.Column(db.DateTime)

class PolityUnit6Progress(db.Model):
    __tablename__='polity_unit6_progress'
    device_id=db.Column(db.String(64),primary_key=True)
    chapter_id=db.Column(db.String(32),primary_key=True)
    completed=db.Column(db.Boolean,nullable=False,default=False)
    updated_at=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

class PolityUnit6Exam(db.Model):
    __tablename__='polity_unit6_exam'
    id=db.Column(db.String(36),primary_key=True)
    device_id=db.Column(db.String(64),nullable=False,index=True)
    questions=db.Column(db.JSON,nullable=False)
    answers=db.Column(db.JSON,nullable=False,default=dict)
    started_at=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    deadline=db.Column(db.DateTime,nullable=False)
    submitted_at=db.Column(db.DateTime)
    score=db.Column(db.Integer)
