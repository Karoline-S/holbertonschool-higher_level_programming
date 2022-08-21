#!/usr/bin/python3
"""send a request to a url using requests package.
print the body of the response if status code is less than 400,
otherwise, print error message
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
