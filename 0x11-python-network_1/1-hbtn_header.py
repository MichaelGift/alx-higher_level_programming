#!/usr/bin/python3
"""
Sends a request to provided URL
Displays the value of 'X-Request-Id' header variable
"""

from sys import argv
from urllib import request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
