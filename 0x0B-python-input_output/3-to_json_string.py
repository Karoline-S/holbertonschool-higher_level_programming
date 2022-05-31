#!/usr/bin/python3
"""a module containing a single function:
to_json_string()
"""

import json


def to_json_string(my_obj):
    """a function to returns the JSON repr of an
    object (string)
    """

    return json.dumps(my_obj)
