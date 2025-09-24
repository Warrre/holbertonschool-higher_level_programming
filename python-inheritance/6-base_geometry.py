#!/usr/bin/python3
"""Defines class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise an Exception because area() is not implemented."""
        raise Exception("area() is not implemented")
