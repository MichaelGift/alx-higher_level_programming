#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

from sys import argv
import requests

if __name__ == "__main__":
    query = {"q": argv[1] if len(argv) > 1 else ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=query)
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
