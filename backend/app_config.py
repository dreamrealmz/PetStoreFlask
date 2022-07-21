import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask

# from flask_swagger import swagger

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'
] = f'postgres://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/{os.environ.get("POSTGRES_NAME")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)
db = SQLAlchemy(app)
