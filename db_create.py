import os.path
from python_cookbook import db, create_app
from python_cookbook.model import Recipe
import config
import ast
import re
import glob


with create_app(config).app_context():
    if not os.path.exists(config.SQLALCHEMY_DATABASE_URI):
        db.create_all()
        print('Created DB')
    else:
        print('DB exists')

    for file in os.listdir(config.PYTHON_RECIPE_FOLDER):
        if os.path.splitext(file)[1] == ".py":
            with open(os.path.join(config.PYTHON_RECIPE_FOLDER, file)) as f:
                raw_text = f.read()
                mod = ast.parse(raw_text)
                doc = ast.get_docstring(mod)

                # Initialise vars
                tags = None
                snippet = None
                author = None
                description = None
                section  = None

                if doc:
                    # First get tags
                    tag_results = re.findall(r"tags:[\t\s\n]+(.*?)(?:\n\s*\n|\Z)",doc, re.IGNORECASE | re.DOTALL)
                    if tag_results:
                        tags = [x.lower().strip() for x in re.split('\n|,',tag_results[0].strip())]

                    # Now the Description
                    description = re.findall(r"description:[\t\s\n]+(.*?)(?:\n\s*\n|\Z)",doc, re.IGNORECASE | re.DOTALL)[0]

                    # Now the Author
                    author = re.findall(r"author:[\t\s\n]+(.*?)(?:\n\s*\n|\Z)",doc, re.IGNORECASE | re.DOTALL)[0]

                    # Now the section
                    section = re.findall(r"section:[\t\s\n]+(.*?)(?:\n\s*\n|\Z)",doc, re.IGNORECASE | re.DOTALL)[0]

                    snippet = re.sub('"""', "", raw_text.replace(doc,""), 2).strip()
                else:
                    snippet = raw_text
                    author = 'Simon Ward-Jones'

                title = os.path.splitext(file)[0]
                recipe = Recipe(title=title,
                                author=author,
                                snippet=snippet,
                                description=description,
                                section=section)

                try:
                    db.session.add(recipe)
                    db.session.commit()
                    print(title)
                except Exception as ex:
                    db.session.rollback()

                    print('Skipped: ' + title)