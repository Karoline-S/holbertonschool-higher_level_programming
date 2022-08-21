#!/usr/bin/python3
"""use github api with personal github credentials to retrieve my user id
"""
import requests
from sys import argv

if __name__ == "__main__":
    username = ""
    token = ""

    if len(argv) >= 3:
        username = argv[1]
        token = argv[2]

    r = requests.get('https://api.github.com/user', auth=(username, token))
    json_data = r.json()
    try:
        print("{}".format(json_data.get('id')))
    except KeyError:
        print("None")
