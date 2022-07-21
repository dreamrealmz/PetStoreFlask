import sys

sys.path.insert(1, '/backend')
from app_config import db  # noqa


class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
