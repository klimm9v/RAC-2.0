from app.app import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    avatar = db.Column(db.String(120), default=None)
    posts = db.relationship("Post", backref="author")
    code = db.Column(db.Integer, unique=True, default=None)
    date_user = db.Column(db.DateTime, default=datetime.now)
    last_online = db.Column(db.DateTime, default=datetime.now)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(100))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_post = db.Column(db.DateTime, default=datetime.now)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False, default=1)
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))