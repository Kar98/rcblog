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


@bp.route('/articles')
def articleIndex():
    g.endpoint = 'articles'
    return render_template('articles.html')

@bp.route('/articles/2021/the-dubious-nature-of-agile')
def article1():
    return render_template('articles/the-dubious-nature-of-agile.html',tags=outputTagsForArticle('the-dubious-nature-of-agile'))

@bp.route('/articles/2021/automation-ins-and-outs')
def article2():
    return render_template('articles/automation-ins-and-outs.html',tags=outputTagsForArticle('automation-ins-and-outs'))

@bp.route('/articles/2021/running-a-good-review')
def article3():
    return render_template('articles/running-a-good-review.html',tags=outputTagsForArticle('running-a-good-review'))

@bp.route('/articles/2022/loadtest-comparison')
def article4():
    return render_template('articles/loadtest-comparison.html',tags=outputTagsForArticle('loadtest-comparison'))

@bp.route('/articles/2022/what-test-tools')
def article5():
    return render_template('articles/what-test-tools.html',tags=outputTagsForArticle('what-test-tools'))
'''
@bp.route('/articles/<year>/<url>')
def getArticle(year,name):
    return render_template('articles/{}'.format(name))
'''