#!/usr/bin/python3
"""a module containing one function:
load_from_json_file()
"""

import json


def load_from_json_file(filename):
    """creates an object from a JSON file
    takes one argument 'filename'
    """

    with open(filename, 'r', encoding="utf-8") as f:
        new_obj = json.load(f)

    return new_obj
