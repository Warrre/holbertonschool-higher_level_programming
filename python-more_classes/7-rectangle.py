#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns the string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        symbol = str(self.print_symbol)
        for i in range(self.__height):
            rect += symbol * self.__width
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Returns a string representation for recreating the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a msg when instance is deleted and updates inst counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
