#!/usr/bin/python3
"""
Module 9-rectangle
Contient la classe Rectangle avec méthode area et __str__
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe Rectangle héritant de BaseGeometry."""

    def __init__(self, width, height):
        """Initialise le rectangle avec validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Retourne une description du rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
