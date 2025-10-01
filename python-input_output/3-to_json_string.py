#!/usr/bin/python3
"""Module for converting a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object."""
    return json.dumps(my_obj)
