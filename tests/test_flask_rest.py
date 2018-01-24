"""Acceptance/Integration tests."""

import json
import os
import tempfile
import pytest
from mini.app import app
from mini.db.adapter import init_db


@pytest.fixture
def client(request):
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        init_db()

    def teardown():
        os.close(db_fd)
        os.unlink(app.config['DATABASE'])
    request.addfinalizer(teardown)

    return client


def test_login(client):
    """Test successful login."""
    result = client.post('/users/login', data=json.dumps({
        'username': app.config['USERNAME'],
        'password': app.config['PASSWORD']
    }), content_type='application/json')

    data = json.loads(result.data)

    assert data[u'logged_in'] is True
    assert type(data[u'visits']) is int


def test_unsucess_login(client):
    """Test unsuccessful login with error."""
    result = client.post('/users/login', data=json.dumps({
        'username': 'notastoredusername',
        'password': 'notastoredusername'
    }), content_type='application/json')

    data = json.loads(result.data)

    assert data[u'message'] == 'User is not in our database'
    assert result.status_code == 404
