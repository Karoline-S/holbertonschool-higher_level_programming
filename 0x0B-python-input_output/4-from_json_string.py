#!/usr/bin/python3
"""a module containing a single function:
from_json_string()
"""

import json


def from_json_string(my_str):
    """returns an object from a JSON string
    takes one required argument
    """

    return json.loads(my_str)
