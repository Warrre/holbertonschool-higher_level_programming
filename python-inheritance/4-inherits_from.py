#!/usr/bin/python3
"""
Module 4-inherits_from
Contient la fonction inherits_from()
"""


def inherits_from(obj, a_class):
    """
    Retourne True si obj est une instance d’une classe qui hérite de a_class
    (et pas a_class lui-même).
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
