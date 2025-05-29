#!/usr/bin/python3
"""
Module 1-my_list
Contient la classe MyList qui hérite de list
"""


class MyList(list):
    """Classe héritée de list, avec méthode print_sorted."""

    def print_sorted(self):
        """Affiche les éléments de la liste triés."""
        print(sorted(self))
