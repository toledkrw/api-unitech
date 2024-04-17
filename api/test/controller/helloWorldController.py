from flask import request, jsonify, Blueprint

test_bp = Blueprint('test', __name__)


@test_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")