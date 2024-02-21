#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    request = requests.get('https://alx-intranet.hbtn.io/status')
    response = request.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
