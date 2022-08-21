#!/usr/bin/python3
"""send a post request to URL using request module, print response body
"""
import requests
from sys import argv

if __name__ == "__main__":
    post_dict = {'email': argv[2]}
    r = requests.post(argv[1], data=post_dict)
    print(r.text)
