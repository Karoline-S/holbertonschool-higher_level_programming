#!/usr/bin/python3
"""a module containing a single function:
save_to_json()
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file in JSON repr
    takes two arguments: my_obj and filename
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
