from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('articles', __name__)

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