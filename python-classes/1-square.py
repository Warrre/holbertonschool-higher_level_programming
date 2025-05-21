#!/usr/bin/python3
"""
Classe Square qui définit un carré par sa taille (size)
"""

class Square:
    """
    Classe représentant un carré
    """

    def __init__(self, size):
        """
        Constructeur de la classe Square

        Arguments :
        size -- la taille du carré (non vérifiée ici)
        """
        self.__size = size
