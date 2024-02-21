#!/usr/bin/python3
"""
Requires GitHub credentials username and password
Uses the GitHub API to display the user id.
"""

from sys import argv
import requests

if __name__ == "__main__":
    auth = (argv[1], argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
