#!/usr/bin/python3
"""Check if obj is an instance or subclass of a_class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or subclass of a_class."""
    return isinstance(obj, a_class)
