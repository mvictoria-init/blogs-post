from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():

    # Crear aplicación de flask
    app = Flask(__name__)

    app.config.from_object('config.Config')
    db.init_app(app)

    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)

    import locale
    locale.setlocale(locale.LC_ALL, 'es_ES')

    # Registrar vistas 
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)

    from blogr import post
    app.register_blueprint(post.bp)

    from .models import User, Post

    with app.app_context():
        db.create_all()

    return app

sqlite = SQLAlchemy()


def create_app2():

    # Crear aplicación de flask
    app = Flask(__name__)

    app.config.from_object('config.Config')
    # db.init_app(app)

    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)

    import locale
    locale.setlocale(locale.LC_ALL, 'es_ES')

    # Registrar vistas 
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)

    from blogr import post
    app.register_blueprint(post.bp)

    from blogr.sqlite3 import config_sqlite
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    sqlite.init_app(app=app)
    
    
    # from .models import User, Post
    from .modelsCopy import User, Post

    with app.app_context():
        sqlite.create_all()

    return app
