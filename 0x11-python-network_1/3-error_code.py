#!/usr/bin/python3
"""sends a request to a URL, prints the response body and handles
HTTPErrors
"""
from urllib import request, parse, error
import sys


if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
