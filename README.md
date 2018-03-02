# python_cookbook
Python recipes

*Python Snipets library*

`tree -I '*__pycache__|venv'`

```
.
├── README.md
├── app.yaml
├── clean_build_run.sh
├── config.py
├── db_create.py
├── db_query.py
├── main.py
├── python_cookbook
│   ├── __init__.py
│   ├── crud.py
│   ├── flask_whooshalchemy.py
│   ├── model.py
│   ├── nav_items.py
│   ├── static
│   │   ├── atom-theme.css
│   │   └── favicon.ico
│   └── templates
│       ├── _form_helpers.html
│       ├── base.html
│       ├── form.html
│       ├── list.html
│       └── view.html
├── python_recipe.sqlite
├── python_recipes
│   ├── aggregate_dataframe.py
│   ├── copy_and_paste.py
│   ├── dataframe_datetime.py
│   ├── dataframe_indexing.py
│   ├── dictionary_from_two_lists.py
│   ├── flask_routing.py
│   ├── flask_sqlalchemy_model.py
│   ├── flatten_list_of_lists.py
│   ├── iterate_on_directory_file_extension.py
│   ├── iterate_on_directory_progress_bar.py
│   ├── list_to_comma_seperated_string.py
│   ├── make_and_delete_directory.py
│   ├── map_functions_on_list.py
│   ├── merge_lists_into_list_of_tuples.py
│   ├── pivot_dataframe.py
│   ├── reduce.py
│   ├── reload_a_module.py
│   ├── run_subprocess.py
│   ├── set_operations.py
│   ├── split_dataframe.py
│   ├── timer.py
│   └── timer_click.py
├── requirements.txt
├── setup.py
└── whoosh_index
    └── Recipe
        ├── MAIN_8y3u26gyhzw493t5.seg
        ├── MAIN_WRITELOCK
        └── _MAIN_311.toc
```


# Depolyment
```bash
sh clean_build_run
gcloud app deploy```


__Note__ It is important to rebuild the database! (probably better to run this in the build - i.e. a bespoke Docker file)