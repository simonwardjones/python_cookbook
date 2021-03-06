"""
Section:
    flask

Author:
    Simon Ward-Jones

Description:
    An example route definition module

Tags:
    flask, routes

"""

from flask import Blueprint, jsonify, \
    render_template, request
from .model import Recipe
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


crud = Blueprint('crud', __name__)


@crud.route("/", methods=['GET', 'POST'])
def list():
    recipes = Recipe.query.all()
    next_page_token = None
    form = SearchForm()
    if request.method == 'POST':
        if form.validate():
            print('Search Hit', request.method, form.query.data)
            recipes = Recipe.query.whoosh_search(form.query.data).all()
            render_template("list.html", recipes=recipes,
                            next_page_token=next_page_token, form=form)
        else:
            return render_template("list.html", recipes=recipes,
                                   next_page_token=next_page_token, form=form)

    return render_template(
        "list.html",
        recipes=recipes,
        next_page_token=next_page_token,
        form=form)


@crud.route('/<id>')
def snippet(id):
    recipe = Recipe.query.get(id)
    return render_template("view.html", recipe=recipe, form=SearchForm())


@crud.route('/<id>/data')
def snippet2(id):
    recipe = Recipe.query.get(id)

    return jsonify({'title': recipe.title,
                    'author': recipe.author,
                    'snippet': recipe.snippet})


class SearchForm(FlaskForm):
    query = StringField('Search', validators=[InputRequired()])
