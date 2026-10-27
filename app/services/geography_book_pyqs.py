"""Printed-book PYQ review intake. Never grants official-release scoring."""
import hashlib
import json
from pathlib import Path
from flask import current_app


def records():
    path = Path(current_app.root_path).parent / 'content/geography/book_pyq_intake.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    rows = data['records']
    if data.get('format') != 'geography-book-pyq-intake-v1' or len({r['id'] for r in rows}) != len(rows):
        raise ValueError('Invalid printed PYQ intake')
    return rows


def question(question_id):
    return next((r for r in records() if r['id'] == question_id), None)


def evidence(record):
    root = Path(current_app.root_path).parent
    allowed = (root / 'content/geography/book_pyq_sources').resolve()
    path = (root / record['source']['evidence_file']).resolve()
    if path.parent != allowed or path.suffix.lower() not in ('.jpg', '.png'):
        raise ValueError('Invalid source evidence path')
    if hashlib.sha256(path.read_bytes()).hexdigest() != record['source']['sha256']:
        raise ValueError('Printed PYQ evidence changed')
    return path


def grade(record, choice):
    # An import claiming scorable=True cannot bypass this review-only boundary.
    return {'status': 'held', 'score': None, 'choice': choice}
