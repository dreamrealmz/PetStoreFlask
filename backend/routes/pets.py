from flask import Blueprint, request
import sys

sys.path.insert(1, '/backend')
from app_config import db  # noqa
from models import Pets, Breeds  # noqa

blueprint = Blueprint('pets', __name__)


@blueprint.route('/pets', methods=['GET', 'POST'])
def pets():
    if request.method == "GET":
        return {
            'result': [
                {
                    'id': pet_id,

                    'name': pet_name,
                    'breed_name': breed_name
                } for pet_id, pet_name, breed_name in db.session.query(Pets.id, Pets.name, Pets.breed_id.name)
            ]
        }

    if request.method == "POST":
        data = request.json
        breed = Breeds.query.filter(Breeds.id == data['breed_id']).first()
        new_pet = Pets(name=data['name'], breed_id=breed.id)
        db.session.add(new_pet)
        db.session.commit()
        return {
            'id': new_pet.id,
            'name': new_pet.name,
            'breed_name': breed.name
        }
