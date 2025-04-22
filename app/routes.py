from flask import Blueprint, render_template
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/users')
def users_page():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)
