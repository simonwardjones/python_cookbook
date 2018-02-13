from python_cookbook.model import Recipe
import collections


def get_nav_items():
    Recipes = Recipe.query.all()
    nav_items = collections.defaultdict(list)
    for i, r in enumerate(Recipes):
        if r.section:
            nav_items[r.section].append({
                "title": r.title,
                "id": r.id
            })
    nav_items = [{"section": x, "recipes": y} for x, y in nav_items.items()]
    # print(nav_items)
    return nav_items
