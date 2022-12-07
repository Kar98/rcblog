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

    print('db config ' + current_app.config['DATABASE'])
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def setupArticles(db):
    print('run setupArticles')
    article1 = "INSERT INTO articles(article_name,tags,article_content) VALUES ('the-dubious-nature-of-agile','agile,software,development','content1');"
    article2 = "INSERT INTO articles(article_name,tags,article_content) VALUES ('automation-ins-and-outs','automation,development','content2');"
    article3 = "INSERT INTO articles(article_name,tags,article_content) VALUES ('running-a-good-review','agile,review','content3');"

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
    print('init db called')
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    #setupArticles(db)


def articleExists(articlename):
    db = get_db()
    rows = db.execute("SELECT tags FROM articles WHERE article_name='{}';".format(articlename)).fetchall()

    if(len(rows) == 0):
        return False
    else:
        return True


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


@click.command('add-tags')
@click.argument('article')
@click.argument('tags')
@with_appcontext
def add_tags(article,tags):
    """Add tags to the system."""
    # IF article exists, then overwrite tags with param. Otherwise add a new record.
    db = get_db()
    if(articleExists(article)):
        qry = "UPDATE articles SET tags = '{}' WHERE article_name = '{}'".format(tags,article)
    else:
        qry = "INSERT INTO articles(article_name,tags,article_content) VALUES ('{}','{}','placeholder');".format(article, tags)

    cur = db.cursor()
    cur.execute(qry)
    db.commit()

    click.echo('Added tags {} to article {}'.format(tags,article))


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(add_tags)
