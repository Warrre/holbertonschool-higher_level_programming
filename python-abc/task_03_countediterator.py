#!/usr/bin/python3
"""
Module contenant la classe CountedIterator.
"""


class CountedIterator:
    """
    Un itérateur qui compte le nombre d'éléments parcourus.

    Cette classe encapsule un itérateur standard et ajoute la fonctionnalité
    de comptage des éléments récupérés via la méthode __next__.
    """

    def __init__(self, iterable):
        """
        Initialise le CountedIterator avec un itérable.

        Args:
            iterable: Un objet itérable (liste, tuple, string, etc.)
                     compter les éléments lors du parcours.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Retourne le nombre d'éléments qui ont été parcourus.

        Returns:
            int: Le nombre d'élément récupéré a la création de l'itérateur.
        """
        return self.count

    def __next__(self):
        """
        Récupère l'élément suivant et incrémente le compteur.

        Cette méthode fait de la classe un itérateur valide en implémentant
        le protocole d'itération Python. Elle incrémente le compteur à chaque
        appel et délègue la récupération de l'élément à l'itérateur.

        Returns:
            L'élément suivant dans la séquence.

        Raises:
            StopIteration: Quand il n'y a plus d'éléments à parcourir.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
