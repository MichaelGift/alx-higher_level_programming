#!/usr/bin/python3
"""
Sends a request to provided URL.
Displays the body of the response on success
Displays error code on failure.
"""

from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
