#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print(f'Body response:\n \
        \t- type: {html}\n \
        \t- content: {type(html)}\n \
        \t- utf8 content: {html.decode()}')
