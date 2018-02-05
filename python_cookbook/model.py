"""
Section:
    Sqlalchemy

Author:
    Simon Ward-Jones

Description:
    An example sqlalchemy table class defenition
"""

from python_cookbook import db
import datetime


class Recipe(db.Model):
    __tablename__ = 'recipes'
    __searchable__ = ['title', 'snippet', 'author', 'description']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    author = db.Column(db.String(128))
    snippet = db.Column(db.Text)
    description = db.Column(db.Text)
    section = db.Column(db.String(128))
    added_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, title, snippet, author, description, section):
        self.title = title
        self.author = author
        self.snippet = snippet
        self.description = description
        self.section = section

