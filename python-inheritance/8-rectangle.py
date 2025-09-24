#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize rectangle with validated width and height.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
