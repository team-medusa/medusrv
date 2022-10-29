import flask

from .. import system

medusa_bp = flask.Blueprint('medusa_bp', __name__, template_folder='../')

@medusa_bp.route('/')
def home():
    return flask.render_template('medusa/templates/home.html')
