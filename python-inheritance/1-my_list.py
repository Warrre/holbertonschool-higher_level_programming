#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list that can print its elements sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
