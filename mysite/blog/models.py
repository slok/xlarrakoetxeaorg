# -*- coding: utf-8 -*-

from blog import db


class Author(db.Model):
    """The Author class, owner of the posts"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    full_name = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
