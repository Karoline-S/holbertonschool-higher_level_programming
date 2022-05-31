#!/usr/bin/python3
"""a module with a single function to save arguments
to a Python list and then save them to a file
"""

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
j_repr = []

try:
    j_repr = load_from_json_file(filename)
except BaseException:
    pass

j_repr = [*j_repr + sys.argv[1:]]

save_to_json_file(j_repr, filename)
