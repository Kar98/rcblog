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
    return render_template('tags.html',articles=foundArticles, tag=tag)


def outputTagsForArticle(article):
    db = get_db()
    try:
        rows = db.execute('SELECT article_name,tags FROM articles;').fetchall()
    except:
        print('no db found')
        rows = []
    foundRow = ''
    for row in rows:
        if article in row[0]:
            foundRow = row[1]
    foundTags = foundRow.split(',')
    print(foundTags)
    return foundTags


@bp.route('/articles/<year>/<title>')
def getArticle(year: str, title: str):
    return render_template(f'articles/{title}.html',tags=outputTagsForArticle(title))


@bp.route('/articles')
def articleIndex():
    g.endpoint = 'articles'
    return render_template('articles.html')
