from flask import Flask,render_template,request,Blueprint,abort,url_for
from jinja2 import TemplateNotFound
from markupsafe import escape
from pyfiles import pagelogic

app = Flask(__name__)


@app.route('/')
def index():
    url_for('static', filename='navbar.css')
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/articles/')
def projects():
    return render_template('articles.html')

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if pagelogic.valid_login(request.form['username'],
                       request.form['password']):
            return pagelogic.do_login(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404




