from app_config import app, db # noqa
from routes import pets_blueprint, swagger_blueprint, swagger_json_blueprint
from models import Pets  # noqa

app.register_blueprint(pets_blueprint)
app.register_blueprint(swagger_json_blueprint)
app.register_blueprint(swagger_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
