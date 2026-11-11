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


class PolityUnit6Override(db.Model):
    """Admin edits/deletes layered over the audited content files at read time; the files are never modified."""
    __tablename__='polity_unit6_override'
    item_id=db.Column(db.String(128),primary_key=True)
    deleted=db.Column(db.Boolean,nullable=False,default=False)
    data=db.Column(db.JSON,nullable=False,default=dict)
    updated_at=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

class PolityUnit6Submission(db.Model):
    """Plain-text questions typed by the admin, to be placed properly later."""
    __tablename__='polity_unit6_submission'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    chapter_id=db.Column(db.String(32),nullable=False,default='')
    text=db.Column(db.Text,nullable=False)
    status=db.Column(db.String(16),nullable=False,default='new')
    created_at=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

class PolityMark(db.Model):
    """A learner's highlights/underlines and bookmark for one page or card (per device)."""
    __tablename__='polity_mark'
    device_id=db.Column(db.String(64),primary_key=True)
    key=db.Column(db.String(200),primary_key=True)
    marks=db.Column(db.JSON,nullable=False,default=list)
    bookmarked=db.Column(db.Boolean,nullable=False,default=False)
    title=db.Column(db.String(300),nullable=False,default='')
    url=db.Column(db.String(500),nullable=False,default='')
    updated_at=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
