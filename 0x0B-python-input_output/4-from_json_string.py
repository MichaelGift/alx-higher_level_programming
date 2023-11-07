#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object from JSON string."""
    return json.loads(my_str)