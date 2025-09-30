import os
from .config import Config
from flask import Flask


def create_app(test_config=None):
    MAX_FILE_SIZE_MB = 16

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # ensure instance and uploads folders exist
    os.makedirs(os.path.dirname(app.config['DATABASE']), exist_ok=True)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import routes
    app.register_blueprint(routes.bp)  
    # app.add_url_rule('/', endpoint='index')
    # app.add_url_rule('/upload', endpoint='upload')
    # app.add_url_rule('/submit', endpoint='submit')
    # app.add_url_rule('/page2', endpoint='page2')

    return app