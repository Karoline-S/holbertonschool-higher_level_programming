#!/usr/bin/python3
"""script that fetches a given URL and prints response
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:\n \
            - type: {}\n \
            - content: {}\n \
            - utf8 content: {}'.format(type(html), html, html.decode()))
