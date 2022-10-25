#!/usr/bin/python3
"""
Module:
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using JSON representation"""

    with open(filename, 'w') as file:
        return file.write(json.dumps(my_obj))
