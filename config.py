import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'python_recipe.sqlite')
PYTHON_RECIPE_FOLDER = os.path.join(basedir, 'python_recipes')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SECRET_KEY = 'hard to guess string'
WOOSH_BASE = 'whoosh'
CSRF_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = True