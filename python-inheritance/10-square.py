#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a square with validated size"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return area of the square"""
        return self.__size ** 2

    def __str__(self):
        """String representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
