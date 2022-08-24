import sys
import flask
from flask import send_file, jsonify, Blueprint
from werkzeug.exceptions import HTTPException
from ..core.utils import get_new_response_error
index = Blueprint('index', __name__)


@index.route('/', methods=['GET'])
@index.route('/home', methods=['GET'])
@index.route('/index', methods=['GET'])
def index_view():
    return f"""
    <div>
        <p>
            Flask app api-db running with version {str(flask.__version__)} Python 
            {'.'.join([str(i) for i in sys.version_info[:2]])} 
        </p> 
    </div>
"""


# -------------------
#   Robots
# -------------------


@index.route('/robots.txt',methods=['GET'])
def robots_txt():
    return send_file('web/static/robots/robots.txt', mimetype='text/plain')

@index.route('/sitemap.xml', methods=['GET'])
def sitemap_xml():
    return send_file('web/static/robots/sitemap.xml', mimetype='application/xml')

# -------------------
#  Error Handlers
# -------------------

@index.errorhandler(404)
def page_not_found(e):
    error = f"""Request route was not found!
    ---------------- ERROR RAW START
    {str(e)}
    ---------------- ERROR RAW END
    """
    return jsonify(get_new_response_error(error, 404, e)), 404

@index.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    error = f"""Server Error!
       ---------------- ERROR RAW START
       {str(e)}
       ---------------- ERROR RAW END
       """
    return jsonify(get_new_response_error(error, code, e)), code