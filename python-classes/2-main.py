#!/usr/bin/python3
Square = __import__('2-square').Square

# Test avec une taille valide
my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

# Test avec la taille par défaut (0)
my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

# Test d'accès direct à l'attribut privé (devrait échouer)
try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

# Test avec une chaîne de caractères (devrait lever TypeError)
try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

# Test avec une valeur négative (devrait lever ValueError)
try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
