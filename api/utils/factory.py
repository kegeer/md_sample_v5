import logging
import sys
from flask import Flask
from flask import jsonify
from flask_swagger import swagger
from api.utils.database import db
from api.utils.response import response_with
import api.utils.response as resp
from api.api_v1 import api as api_blueprint

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

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

    db.init_app(app)
    with app.app_context():
        db.create_all()

    logging.basicConfig(stream=sys.stdout,
                        format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
                        level=logging.DEBUG)
    return app
