import logging
import sys
from flask import Flask
from flask import jsonify
from flask_swagger import swagger
from api.utils.database import db
from api.utils.response import response_with
import api.utils.response as resp
from instance.config import app_config
from flask_cors import CORS

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, supports_credentials=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)


    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)

    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.NOT_FOUND_HANDLER_404)

    @app.route('/api/v1.0/spec')
    def spec():
        swag = swagger(app, prefix='/api/v1.0')
        swag['info']['version'] = '1.0'
        swag['info']['title'] = 'Flask Sample Api'
        return jsonify(swag)

    logging.basicConfig(stream=sys.stdout,
                        format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
                        level=logging.DEBUG)
    from api.api_v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
