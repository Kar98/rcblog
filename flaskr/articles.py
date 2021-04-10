from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('articles', __name__)

@bp.route('/articles')
def articleIndex():
    g.endpoint = "articles"
    return render_template("articles.html")

