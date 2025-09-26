#!/usr/bin/python3
"""
Module contenant les classes SwimMixin, FlyMixin et Dragon.
"""


class SwimMixin:
    """
    Mixin qui fournit la capacité de nager.
    """

    def swim(self):
        """Affiche le comportement de nage."""
        print("The creature swims!")


class FlyMixin:
    """
    Mixin qui fournit la capacité de voler.
    """

    def fly(self):
        """Affiche le comportement de vol."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon qui peut nager, voler et rugir.
    """

    def roar(self):
        """Affiche le rugissement du dragon."""
        print("The dragon roars!")
