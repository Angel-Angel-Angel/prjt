""" user routes """

from flask import Blueprint, render_template
from app.models import User

user_bp = Blueprint('users', __name__)

@user_bp.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)
