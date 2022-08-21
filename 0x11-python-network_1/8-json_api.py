#!/usr/bin/python3
"""takes in a letter, sends a POST request to a URL with letter as param,
prints json response or no result
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) >= 2:
        post_data = {'q': argv[1]}
    else:
        post_data = {'q': ""}

    r = requests.post('http://0.0.0.0:5000/search_user', post_data)
    try:
        json_data = r.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
