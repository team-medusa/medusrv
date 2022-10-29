"""Initializes the Flask server."""

import logging
import flask

from dotenv import load_dotenv
from . import admin

load_dotenv()

def create_app():
    """Prepare and run the Flask app."""
    app = flask.Flask(__name__, static_url_path='/static', static_folder='static/')
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    from .medusa.medusa import medusa_bp

    app.register_blueprint(medusa_bp)

    import flaskcode

    app.config.from_object(flaskcode.default_config)

    app.config['FLASKCODE_RESOURCE_BASEPATH'] = '/home/python/web/medusrv/container'

    app.register_blueprint(flaskcode.blueprint, url_prefix='/editor')

    @app.context_processor
    def injector():
        return dict(home_url='https://onlix.me')

    return app
