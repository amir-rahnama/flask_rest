"""A blueprint that handles user related functions."""
from flask import Blueprint, request, render_template, jsonify
from mini.db import adapter


bp = Blueprint('users', __name__, static_folder='static')


@bp.route('/login', methods=['POST'])
def login():
    """Provide login for user."""
    # Check valid login
    data = request.get_json()
    username = data[u'username']
    password = data[u'password']

    user = adapter.get_user(username, password)

    if not user:
        response = jsonify({'message': 'User is not in our database'})
        response.status_code = 404

        return response

    # incremenet users visit
    visits = adapter.increment_visit(username)

    return jsonify({'logged_in': True, 'visits': visits})


@bp.route('/')
def index():
    """Render login."""
    return render_template('login.html')


@bp.route('/login/<username>')
def user_login_count(username):
    """Show counts of users login."""
    visit = adapter.get_user_visit(username)[0]
    return jsonify({username: username, 'visits': visit})


@bp.route('/register', methods=['POST'])
def register_user():
    """Register users."""
    data = request.get_json()
    username = data[u'username']
    password = data[u'password']

    inserted = adapter.insert_user(username, password)

    if inserted:
        response = jsonify({username: username, 'created': True})
        response.status_code = 200
    else:
        response = jsonify({username: username, 'created': False,
                            'message': 'Username is already \
                            registered in database'})
        response.status_code = 404

    return response
