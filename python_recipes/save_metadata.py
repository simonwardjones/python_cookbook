"""
Section:
    Reading and Writing

Author:
    Carlos Aguilar

Description:
    Add metadata information to files, so they can be easily summarised, ie: latest version, contents, ways of generating
    or ways of using it.

Tags:
    write, metadata, json
"""

import os
import json
import datetime as dt


def save_metadata(file_path, short_description, file_comments,
                  file_generation, file_directions):
    """Save file meta information

    Add useful information about the file as a json summary.

    Args:
        file_path (str): Current path to the file.
        short_description (str): Brief description of the file.
        file_comments (str): A bit more detailed description.
        file_generation (str): How was the file generated.
        file_directions (str): How to use the file or what to expect when loaded.


    Category: Python
    Topic: Metadata

    """

    stat_info = os.stat(file_path)
    size_MB = round(statinfo.st_size / (10**6))
    [fPath, fName] = os.path.split(file_path)

    format = '%d_%m_%Y_%H_%M_%S'
    creation_time = dt.datetime.today().strftime(format)

    metadata = {'description': short_description,
                'comments': file_comments,
                'filename': fName,
                'folder': fPath,
                'creationTime': creation_time,
                'directions': file_directions,
                'generation': file_generation,
                'sizeMB': sizeMB}

    jsonFName = file_path.replace(os.path.splitext(fName)[1], '.json')
    with open(jsonFName, 'w') as outfile:
        json.dump(metadata, outfile)


"""
Example:
    shortDescription = 'CatBoost model'
    fileComments     = '''This file includes a catboost model to predict the number of coffees that the Data Science team consumes in a week'''
    fileGeneration   = 'File generated with ' + os.path.abspath(__file__) + '(the script)'
    fileDirections   = '''This pickle file will get loaded as a dataframe of size ''' + \
    str(model.shape) + \
    '''. Read this data with utils.readPickleFile(current_model);'''
    filePath = current_model

    saveMetadata(filePath, shortDescription, fileComments, \
        fileGeneration, fileDirections)
"""
