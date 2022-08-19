#!/usr/bin/python3
"""script that fetches a passed in URL and prints
required header field
"""
from sys
from urllib import request, parse

if __name__ == "__main__":
    post_dict = {"email": sys.argv[2]}
    encoded_data = parse.urlencode(post_dict)
    post_data = encoded_data.encode("utf-8")
    new_request = request.Request(sys.argv[1], post_data)
    with request.urlopen(new_request) as response:
        html = response.read()
        print(html.decode('utf-8')
