"""Entry module for Flask."""
import os
from flask import Flask, g
from werkzeug.utils import find_modules, import_string
from mini.db.adapter import init_db
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'db', 'mini.db'),
    DEBUG=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('MINI_SETTINGS', silent=True)


def register_blueprints():
    """Register all service modules."""
    for name in find_modules('mini.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp, url_prefix='/' + mod.bp.name)
    return None


@app.cli.command('initdb')
def initdb_command():
    """Create the database tables."""
    init_db()
    print('Initialized the database.')


@app.teardown_appcontext
def close_db(error):
    """Close the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


register_blueprints()
