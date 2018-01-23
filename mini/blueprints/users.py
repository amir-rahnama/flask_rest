from flask import Blueprint, request, render_template
from mini.db import adapter


bp = Blueprint('users', __name__, static_folder='static')


@bp.route('/login', methods=['POST'])
def login():
    """Provide login for user."""
    # Check valid login
    # increment visit
    print(adapter.get_user(request.form['username'], request.form['password']))


@bp.route('/')
def index():
    # return bp.send_static_file('index.html')
    return render_template('login.html')
