#!/usr/bin/python3
"""use github api with personal github credentials to retrieve commits on
a given repo. Print last 10 commits from most recent to oldest
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) >= 3:
        repo_name = argv[1]
        owner_name = argv[2]
    else:
        repo_name = owner_name = ""

    queryurl = "https://api.github.com/repos/{}/{}/commits". \
        format(repo_name, owner_name)
    r = requests.get(queryurl)
    json_data = r.json()
    try:
        i = 0
        for i in range(10):
            r_dict = json_data[i]
            print("{}: {}".format(r_dict['sha'], \
                                  r_dict['commit']['author']['name']))
    except Exception:
        print("None")
