"""DB adaper for the app."""
from sqlite3 import dbapi2 as sqlite3
from flask import g, current_app


def connect_db():
    """Connect to the specific database."""
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initialize the database."""
    db = get_db()
    with current_app.open_resource('db/schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def get_db():
    """Open a new database connection if there is none."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def get_user(username, password):
    """Select user by username and password."""
    db = get_db()
    cur = db.execute('select username, password from users where \
      username=? AND password=?', (username, password))
    entries = cur.fetchone()
    return entries


def get_user_visit(username):
    """Select users visit by username."""
    db = get_db()
    cur = db.execute('select counter from visits where username=?',
                     (username,))
    entries = cur.fetchone()
    return entries


def set_user_in_visits_table(username, visit):
    """Set users visit."""
    db = get_db()
    db.execute('insert into visits (username, counter) values \
         (?, ?)', (username, 1))
    db.commit()

    return 1


def insert_user(username, password):
    """Inser new users."""
    db = get_db()
    try:
        db.execute('insert into users (username, password) values \
         (?, ?)', (username, password))
        db.commit()
        created = True
    except sqlite3.IntegrityError as e:
        created = False

    return created


def update_user_visit(username, visit):
    """Update the visit count of a user."""
    new_visit = visit + 1
    db = get_db()
    db.execute('update visits set counter=? where \
      username=?', (new_visit, username))
    db.commit()

    return new_visit


def increment_visit(username):
    """Select users visit by one."""
    visit = get_user_visit(username)
    no_visit = type(visit) is not sqlite3.Row

    if (no_visit):
        visit = 0
        return set_user_in_visits_table(username, visit)

    return update_user_visit(username, visit[0])
