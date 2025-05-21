#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))        # Affiche le type de l'objet
print(my_square.__dict__)     # Affiche les attributs (ici vide)
