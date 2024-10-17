from flask import Blueprint
from controllers import controllers

bp = Blueprint('routes', __name__)

@bp.route('/teste', methods=['GET'])
def home():
    return 'Api is Working'

@bp.route('/api/v1/predict', methods=['POST'])
def inferencia():
    return controllers.inferencia()
