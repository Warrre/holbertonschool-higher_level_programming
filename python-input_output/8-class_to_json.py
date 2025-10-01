#!/usr/bin/python3
"""Module for converting a class instance to a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of a simple data structure."""
    return obj.__dict__
