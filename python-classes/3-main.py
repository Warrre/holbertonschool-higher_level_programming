#!/usr/bin/python3
Square = __import__('3-square').Square

# Création d'un carré avec la taille 3
my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

# Tentative d'accès direct à l'attribut privé (provoque une erreur)
try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

# Création d'un autre carré avec la taille 5
my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
