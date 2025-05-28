#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
