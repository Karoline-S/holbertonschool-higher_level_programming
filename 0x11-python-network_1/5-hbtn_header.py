#!/usr/bin/python3
"""get a URL using requests package, print content type and content
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
