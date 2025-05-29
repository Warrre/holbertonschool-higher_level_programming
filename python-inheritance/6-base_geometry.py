#!/usr/bin/python3
"""
Module 6-base_geometry
Contient la classe BaseGeometry avec une méthode area
"""


class BaseGeometry:
    """Classe BaseGeometry avec méthode area non implémentée."""

    def area(self):
        """Lève une exception car area n'est pas implémentée."""
        raise Exception("area() is not implemented")
