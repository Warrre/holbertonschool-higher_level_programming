#!/usr/bin/python3
"""Module for load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
