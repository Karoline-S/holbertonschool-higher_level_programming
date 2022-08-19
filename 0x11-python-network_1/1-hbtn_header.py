#!/usr/bin/python3
"""script that fetches a passed in URL and prints
required header field
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.getheader("X-Request-Id")
        print(header)
