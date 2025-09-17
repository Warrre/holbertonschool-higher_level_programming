#!/usr/bin/python3
"""
    This module defines a class Square that represents a square by its size
    and position, with methods to compute its area and print it using the
    '#' character, offset by the specified position
"""


class Square:
    """Class that defines a square by its size"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square
        Args:
            size (int): size of the square must be an integer >= 0
            position (tuple): position must be a tuple of 2 positive integers
        """
        self.__size = size
        self.position = position

    def area(self):
        """
        Calculate and return the area of the square
        Returns: int: The area of the square (size * size)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the current size of the square
        Returns: int: The current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation
        Args: value (int): The new size of the square. Must be an integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation
        Args: value (int): The position of the square. Must be an integer >= 0
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square with '#' and uses position for indentation
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
