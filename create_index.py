import os.path
import ast
import re
import json

PYTHON_RECIPE_FOLDER = './python_recipes'

INDEX = []
for file in os.listdir(PYTHON_RECIPE_FOLDER):

    if os.path.splitext(file)[1] == ".py":
        print(file)
        with open(os.path.join(PYTHON_RECIPE_FOLDER, file)) as f:
            raw_text = f.read()
            mod = ast.parse(raw_text)
            doc = ast.get_docstring(mod)

        # Initialise vars
        tags = None
        snippet = None
        author = None
        description = None
        section = None

        if doc:
            # First get tags
            # DOTALL matches all including \n!
            tag_results = re.findall(
                r"tags:[\t\s\n]+(.*?)(?:\n\s*\n|\Z)",
                doc,
                re.IGNORECASE | re.DOTALL)
            if tag_results:
                tags = [x.lower().strip()
                        for x in re.split('\n|,', tag_results[0].strip())]

            # Now the Description the regexp finds everythin
            description = re.findall(
                r"description:[\t\s\n]+(.*?)(?:\n\s*\n|\Z)",
                doc,
                re.IGNORECASE | re.DOTALL)[0]

            # Now the Author
            author = re.findall(
                r"author:[\t\s\n]+(.*?)(?:\n\s*\n|\Z)",
                doc,
                re.IGNORECASE | re.DOTALL)[0]

            # Now the section
            section = re.findall(
                r"section:[\t\s\n]+(.*?)(?:\n\s*\n|\Z)",
                doc,
                re.IGNORECASE | re.DOTALL)[0]

            snippet = re.sub(
                '"""', "", raw_text.replace(doc, ""), 2).strip()
        else:
            snippet = raw_text
            author = 'Simon Ward-Jones'

        title = os.path.splitext(file)[0]
        title = title.replace('-', ' ')
        title = title.replace('_', ' ')
        recipes = dict(title=title.capitalize(),
                       author=author.title(),
                       snippet=snippet,
                       description=description,
                       section=section.title(),
                       tags=tags)
        INDEX.append(recipes)

with open('index.json', 'w') as f:
    f.write(json.dumps(INDEX))
