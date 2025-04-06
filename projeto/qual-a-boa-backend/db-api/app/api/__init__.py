from flask import Blueprint
from .auth import auth_bp
from .restaurants import restaurants_bp

api_bp = Blueprint('api', __name__)

api_bp.register_blueprint(auth_bp, url_prefix='/auth')
api_bp.register_blueprint(restaurants_bp, url_prefix='/restaurants') 