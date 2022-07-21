from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('swagg', __name__)

api = Api(
    blueprint,
    title='Swagger Petstore',
    version='1.0.1',
    description='',
    doc='/docs',
)