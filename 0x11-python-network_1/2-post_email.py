#!/usr/bin/python3
"""script that fetches a passed in URL and prints
required header field
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        message_body = response.read().decode('utf-8')
        print(message_body)
