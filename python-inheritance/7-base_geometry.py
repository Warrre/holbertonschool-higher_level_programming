#!/usr/bin/python3
"""
Module 7-base_geometry
Contient la classe BaseGeometry avec validation d'entiers
"""


class BaseGeometry:
    """Classe BaseGeometry avec méthodes area et integer_validator."""

    def area(self):
        """Lève une exception car area n'est pas implémentée."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que value est un entier > 0.
        - name : nom du paramètre (str)
        - value : valeur à valider (int)
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
