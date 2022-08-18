#!/usr/bin/python3
""" script that fetches a given URL """
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print(f'Body response:\n \
            \t- type: {type(html)}\n \
            \t- content: {html}\n \
            \t- utf8 content: {html.decode()}')
