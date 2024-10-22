from blogr import sqlite
class User(sqlite.Model):
    __tablename__ = 'users'
    id = sqlite.Column(sqlite.Integer, primary_key=True)
    username = sqlite.Column(sqlite.String(50), nullable=False)
    email = sqlite.Column(sqlite.String(120), unique=True, nullable=False)
    password = sqlite.Column(sqlite.Text, nullable=False)
    photo = sqlite.Column(sqlite.String(200))

    def __init__(self, id, username, email, password, photo = None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.photo = photo

    def __repr__(self):
        return f"User: '{self.username}'"
    
from datetime import datetime

class Post(sqlite.Model):
    __tablename__ = 'posts'
    id = sqlite.Column(sqlite.Integer, primary_key=True)
    author = sqlite.Column(sqlite.Integer, sqlite.ForeignKey('users.id'), nullable=False)
    url = sqlite.Column(sqlite.String(100), unique = True, nullable=False)
    title = sqlite.Column(sqlite.String(100), nullable=False)
    info = sqlite.Column(sqlite.Text)
    content = sqlite.Column(sqlite.Text)
    created = sqlite.Column(sqlite.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, id, author, url, title, info, content) -> None:
        self.id = id
        self.author = author
        self.url = url
        self.title = title
        self.info = info
        self.content = content

    def __repr__(self) -> str:
        return f'Post: {self.title}'
