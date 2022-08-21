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
    for commits in json_data[:10]:
        print("{}: {}". \
              format(commits['sha'], commits['commit']['author']['name']))
