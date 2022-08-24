import os
from flask import Flask
from .config import app_config
from flask_restful import Resource, Api
from flask import got_request_exception
from .core.logger import create_logger, LOG_ERRORS, log_exception
from .Resources.routes import register_routes


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logger = create_logger(__name__)

def build() -> tuple:
    app = Flask(__name__, static_folder='web/static', template_folder='web/templates')
    app_config.load_configs(app, BASE_DIR)
    api = Api(app,  catch_all_404s=True, errors=LOG_ERRORS)
    got_request_exception.connect(log_exception, app)

    with app.app_context():
        # =============== < BLUEPRINTS ROUTES > =============== #
        from .controllers import index
        app.register_blueprint(index.index)

        # =============== < RESOURCES ROUTES > =============== #
        register_routes(api)

    return app, api

app, api  = build()
