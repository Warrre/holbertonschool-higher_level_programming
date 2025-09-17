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

    @property
    def size(self):
        """Get the current size of the square"""
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

    def my_print(self):
        """
        Prints the square with the character '#' to the standard output
        If the size is 0, prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
