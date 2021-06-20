import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def setupArticles(db):
    article1 = "INSERT INTO articles(article_name,tags,article_content) VALUES ('agile','agile,software,development','content1');"
    article2 = "INSERT INTO articles(article_name,tags,article_content) VALUES ('automation-ins-and-outs','automation,development','content2');"
    article3 = "INSERT INTO articles(article_name,tags,article_content) VALUES ('running-a-good-review','agile,review','content1');"

    cur = db.cursor()

    eid = cur.execute(article1)
    db.commit()
    print('executed {}'.format(eid))

    eid = cur.execute(article2)
    db.commit()
    print('executed {}'.format(eid))

    eid = cur.execute(article3)
    db.commit()
    print('executed {}'.format(eid))

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    setupArticles(db)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
