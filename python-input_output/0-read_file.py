#!/usr/bin/python3
"""Module for reading and printing a UTF-8 text file."""


def read_file(filename=""):
    """Reads a text file and prints its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
