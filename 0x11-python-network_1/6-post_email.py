#!/usr/bin/python3
"""
Sends a POST request to the provided URL with email parameter
Displays the body of the response.
"""

from sys import argv
import requests

if __name__ == "__main__":
    print(requests.post(argv[1], data={'email': argv[2]}).text)
