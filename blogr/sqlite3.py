from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .models import User, Post
from .modelsCopy import User as User2, Post as Post2

def config_sqlite(app:Flask, sqlite:SQLAlchemy):

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    print('objjj ',sqlite)
    sqlite.init_app(app=app)
    
    with app.app_context():
        sqlite.create_all()

def get_users(app:Flask) -> list[User]:
    with app.app_context():
        return User.query.all()

def get_post(app:Flask) -> list[Post]:
    with app.app_context():
    
        return Post.query.all()


def transferir_datos(sqlite:SQLAlchemy, app:Flask, app2:Flask):
    users = get_users(app=app)
    print('users: ', users)
    posts = get_post(app=app)
    print('posts: ',posts)
    with app2.app_context():
        for user in users:
            nUser = User2(id=user.id,
                        username=user.username, 
                        email=user.email, 
                        password=user.password, 
                        photo=user.photo)
            sqlite.session.add(nUser)

        for post in posts:
            nPost = Post2(id=post.id, 
                        author=post.author, 
                        url=post.url,
                        title=post.title,
                        info=post.info, 
                        content=post.content)
            sqlite.session.add(nPost)
        sqlite.session.commit()