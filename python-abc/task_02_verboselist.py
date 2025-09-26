#!/usr/bin/python3
"""
Module contenant la classe VerboseList qui étend la classe list de Python.
"""


class VerboseList(list):
    """
    Une class qui étend la class list de Python avec des notification verbale.

    Cette classe affiche des messages informatifs chaque fois qu'un élément
    est ajouté ou supprimé de la liste.
    """

    def append(self, obj):
        """
        Ajoute un élément à la fin de la liste avec notification.

        Args:
            obj: L'élément à ajouter à la liste.
        """
        super().append(obj)
        print("Added [{}] to the list.".format(obj))

    def extend(self, obj):
        """
        Étend la liste avec les éléments d'un itérable avec notification.

        Args:
            obj: Un itérable dont les éléments seront ajoutés à la liste.
        """
        count = len(obj)
        super().extend(obj)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, value):
        """
        Supprime la première occurrence d'une valeur avec notification.

        Args:
            value: La valeur à supprimer de la liste.

        Raises:
            ValueError: Si la valeur n'est pas trouvée dans la liste.
        """
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        """
        Supprime et retourne un élément à l'index donné avec notification.

        Args:
            index (int, optional): L'index de l'élément à supprimer.
                                 Par défaut -1 (dernier élément).

        Returns:
            L'élément supprimé de la liste.

        Raises:
            IndexError: Si l'index est hors limites.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
