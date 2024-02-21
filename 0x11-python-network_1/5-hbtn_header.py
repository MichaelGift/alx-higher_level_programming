#!/usr/bin/python3
"""
Sends a request to provided URL
Displays the value of 'X-Request-Id' in response header.
"""

from sys import argv
import requests

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
