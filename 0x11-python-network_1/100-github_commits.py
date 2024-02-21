#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest)
From the repository “rails” by the user “rails”.
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10" \
        .format(argv[2], argv[1])
    response = requests.get(url)
    results = response.json()
    for commit in results:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
