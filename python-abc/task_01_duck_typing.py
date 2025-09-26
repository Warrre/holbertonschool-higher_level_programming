#!/usr/bin/python3
"""
Module démontrant le concept de Duck Typing avec des formes géométriques.
"""
import math

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.

    Cette classe définit l'interface que toutes les formes doivent implémenter.
    """

    @abstractmethod
    def area(self):
        """
        Calcule l'aire de la forme.

        Returns:
            float: L'aire de la forme.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calcule le périmètre de la forme.

        Returns:
            float: Le périmètre de la forme.
        """
        pass


class Circle(Shape):
    """
    Classe représentant un cercle.
    """

    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon donné.

        Args:
            radius (float): Le rayon du cercle (valeur absolue utilisée).
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calcule l'aire du cercle.

        Returns:
            float: L'aire du cercle (π × r²).
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calcule le périmètre du cercle.

        Returns:
            float: Le périmètre du cercle (2 × π × r).
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Classe représentant un rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Args:
            width (float): La largeur du rectangle.
            height (float): La hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            float: L'aire du rectangle (largeur × hauteur).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            float: Le périmètre du rectangle (2 × (largeur + hauteur)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Affiche les informations d'une forme (aire et périmètre).

    Cette fonction utilise le Duck Typing - elle accepte tout objet
    qui a les méthodes area() et perimeter().

    Args:
        shape: Un objet ayant les méthodes area() et perimeter().
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
