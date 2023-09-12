#!/usr/bin/python3
# 6-from_json_string.py
"""Write a function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """Return the Python object of a JSON string."""
    return json.loads(my_str)
