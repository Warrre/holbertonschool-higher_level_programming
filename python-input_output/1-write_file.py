#!/usr/bin/python3
"""Module for reading and printing a UTF-8 text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
