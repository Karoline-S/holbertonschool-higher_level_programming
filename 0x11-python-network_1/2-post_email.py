#!/usr/bin/python3
"""script that fetches a passed in URL and prints
required header field
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    post_dict = {'email': argv[2]}
    post_data = urllib.parse.urlencode(post_dict)
    encoded_data = post_data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], encoded_data)

    with urllib.request.urlopen(req) as response:
        msg_body = response.read().decode('utf-8')
        print(msg_body)
