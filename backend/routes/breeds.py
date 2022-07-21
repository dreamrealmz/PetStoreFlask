from flask import Blueprint, request
import sys

sys.path.insert(1, '/backend')
from app_config import db  # noqa
from models import Breeds  # noqa

blueprint = Blueprint('breeds', __name__)


@blueprint.route('/breeds', methods=['GET', 'POST'])
def breeds():
    if request.method == "GET":
        return {
            'result': [
                {
                    'id': breed_id,
                    'name': breed_name,
                } for breed_id, breed_name in db.session.query(Breeds.id, Breeds.name)
            ]
        }
    if request.method == "POST":
        try:
            data = request.json
            new_breed = Breeds(name=data['name'])
            db.session.add(new_breed)
            db.session.commit()
            return {
                'id': new_breed.id,
                'name': new_breed.name
            }
        except Exception as error:
            return {'error': f'{error}'}