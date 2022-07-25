import sys

sys.path.insert(1, '/backend')
from app_config import db  # noqa


class Breeds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    pets = db.relationship('Pets', backref='breed', lazy=True)
    # pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'),
    #     nullable=False)
