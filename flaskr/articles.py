from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

bp = Blueprint('articles', __name__)

@bp.route('/articles/tags/<tag>')
def getTags(tag: str):
    db = get_db()
    # Click on tag
    # Code will look up all articles
    rows = db.execute('SELECT * FROM articles;').fetchall()
    foundTags = []
    foundArticles = []

    for row in rows:
        if tag in row[2]:
            foundTags.append(tag)
            foundArticles.append(row[1])

    # If an article contains the expected tag, then output
    print(foundArticles)
    return render_template('tags.html',articles=foundArticles)


@bp.route('/articles')
def articleIndex():
    g.endpoint = 'articles'
    return render_template('articles.html')

@bp.route('/articles/2021/agile')
def article1():
    return render_template('articles/agile.html')

@bp.route('/articles/2021/automation-ins-and-outs')
def article2():
    return render_template('articles/automation-ins-and-outs.html')

@bp.route('/articles/2021/running-a-good-review')
def article3():
    return render_template('articles/running-a-good-review.html')
