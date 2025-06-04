#!/usr/bin/python3
"""Module for CSV serialization"""
import csv
import json


def convert_csv_to_json(filename):
    """Converts a CSV file to a JSON file"""
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", "w") as file:
            json.dump(data, file)

        return True
    except Exception:
        return False
