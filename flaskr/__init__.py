import os

from flask import Flask, render_template, g, request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='static')
    #Mobility(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def index():
        g.endpoint = "index"
        return render_template('index.html')

    @app.route('/about')
    def about():
        g.endpoint = "about"
        return render_template('about.html')

    @app.route('/search')
    def search():
        g.endpoint = "search"
        return render_template('search.html')
    
    @app.route('/test')
    def test():
        g.endpoint = 'test'
        return render_template('test.html')

    from . import db
    db.init_app(app)
    #db.init_db_command()

    from . import auth,articles,api
    app.register_blueprint(auth.bp)
    app.register_blueprint(articles.bp)
    app.register_blueprint(api.bp)

    return app