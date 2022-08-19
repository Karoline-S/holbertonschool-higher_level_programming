#!/usr/bin/python3
"""script that fetches a passed in URL and prints
required header field
"""
import urllib.request
import urllib.parse
from sys


if __name__ == "__main__":

    url = sys.argv[1]
    post_dict = {'email': sys.argv[2]}
    post_data = urllib.parse.urlencode(post_dict)
    encoded_data = post_data.encode('ascii')
    req = urllib.request.Request(url, encoded_data)

    with urllib.request.urlopen(req) as response:
        msg_body = response.read().decode('utf-8')
        print(msg_body)
