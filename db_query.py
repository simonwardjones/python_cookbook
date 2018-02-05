import os.path
from python_cookbook import db, create_app
from python_cookbook.model import Recipe
import config
import flask_whooshalchemy as whooshalchemy

app = create_app(config)


# # # Ad hoc querying the db
# with app.app_context():
#     Recipes = Recipe.query.all()
#     for i, r in enumerate(Recipes):
#         print(str(i+1), r.title, r.snippet)
#     b = Recipe.query.whoosh_search('flask')
#     print(b)
#     Recipes_whoosh = Recipe.query.whoosh_search('flask').all()
#     for i, r in enumerate(Recipes_whoosh):
#         print(str(i+1),r.__dict__)


# def rebuild_index(model, app):
#     primary_field = model.pure_whoosh.primary_key_name
#     searchables = model.__searchable__
#     index_writer = whooshalchemy.whoosh_index(app, model)
#     with app.app_context():
#         query = model.query.all()
#         with index_writer.writer() as writer:
#             for recipe in query:
#                 index_attrs = {}
#                 for field in searchables:
#                     index_attrs[field] = str(getattr(recipe, field))
#                 index_attrs[primary_field] = str(getattr(recipe, primary_field))
#                 print(index_attrs)
#                 writer.update_document(**index_attrs)

# rebuild_index(Recipe,app)

with app.app_context():
    Recipes = Recipe.query.all()
    for i, r in enumerate(Recipes):
        print(str(i+1), r.title, r.snippet)