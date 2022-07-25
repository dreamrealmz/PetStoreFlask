import sys

sys.path.insert(1, '/backend')
from app_config import db  # noqa


class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    breed_id = db.Column(db.Integer, db.ForeignKey('breeds.id'), nullable=False)
