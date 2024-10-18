# blueprints/user/__init__.py
from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def list_users():
    return "List of users"
