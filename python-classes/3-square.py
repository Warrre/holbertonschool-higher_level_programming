#!/usr/bin/python3
"""
    Module that defines a Square class with a private size attribute
"""


class Square:
    """Class that defines a square by its size"""
    def __init__(self, size=0):
        """
        Initialize a new Square
        Args: size (int): size of the square must be an integer >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square
        Returns: int: The area of the square
        """
        return self.__size ** 2
    