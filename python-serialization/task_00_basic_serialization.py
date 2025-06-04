#!/usr/bin/python3
"""Module for basic serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes data to a file"""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes data from a file"""
    with open(filename, "r") as f:
        return json.load(f)
