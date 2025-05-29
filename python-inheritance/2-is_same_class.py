#!/usr/bin/python3
"""
Module 2-is_same_class
Contient la fonction is_same_class()
"""


def is_same_class(obj, a_class):
    """Retourne True si obj est une instance exacte de a_class."""
    return type(obj) is a_class
