#!/usr/bin/python3
"""
Module démontrant l'héritage multiple.
"""


class Fish:
    """
    Classe représentant un poisson.

    Cette classe définit les comportements de base d'un poisson.
    """

    def swim(self):
        """
        Affiche le comportement de nage du poisson.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Affiche l'habitat du poisson.
        """
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau.

    Cette classe définit les comportements de base d'un oiseau.
    """

    def fly(self):
        """
        Affiche le comportement de vol de l'oiseau.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Affiche l'habitat de l'oiseau.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant qui hérite de Fish et Bird.

    Cette classe démontre l'héritage multiple en combinant les capacités
    d'un poisson et d'un oiseau, tout en surchargeant leurs méthodes
    avec des comportements spécifiques au poisson volant.
    """

    def swim(self):
        """
        Affiche le comportement de nage spécifique au poisson volant.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Affiche le comportement de vol spécifique au poisson volant.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Affiche l'habitat spécifique au poisson volant.

        Surcharge les méthodes habitat() de Fish et Bird pour refléter
        la nature hybride du poisson volant.
        """
        print("The flying fish lives both in water and the sky!")

    def __mro__(self):
        print(FlyingFish.mro())
