#!/usr/bin/python3
"""
Sends a POST request to the provided URL and email as a parameter
Displays the body of the response (decoded in utf-8)
"""

from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    email = parse.urlencode({"email": argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], email) as page:
        print(page.read().decode('utf-8'))
