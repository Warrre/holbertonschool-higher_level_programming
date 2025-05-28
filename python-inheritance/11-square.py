#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialisation du carré avec une taille"""
        self.integer_validator("size", size)
        self.__size = size
        # Appelle le constructeur de Rectangle avec width et height égaux à size
        super().__init__(size, size)

    def area(self):
        """Retourne l'aire du carré"""
        return self.__size ** 2

    def __str__(self):
        """Retourne la représentation du carré"""
        return "[Square] {}/{}".format(self.__size, self.__size)
