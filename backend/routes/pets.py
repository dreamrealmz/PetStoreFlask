from flask import Blueprint, request
import sys

sys.path.insert(1, '/backend')
from app_config import db  # noqa
from models import Pets  # noqa

blueprint = Blueprint('pets', __name__)


@blueprint.route('/pets', methods=['GET', 'POST'])
def pets():
    if request.method == "GET":
        return {
            'result': [
                {
                    'id': pet_id,
                    'name':pet_name,
                } for pet_id, pet_name in db.session.query(Pets.id, Pets.name)
            ]
        }
    if request.method == "POST":
        data = request.json
        new_pet = Pets(name=data['name'])
        db.session.add(new_pet)
        db.session.commit()
        return {
            'id': new_pet.id,
            'name': new_pet.name
        }
