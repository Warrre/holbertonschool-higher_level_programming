Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))  # Affiche le type : <class '1-square.Square'>
print(my_square.__dict__)  # Affiche tous les attributs de l'objet

# Essaie d'accéder à size (ça va échouer car il est privé)
try:
    print(my_square.size)
except Exception as e:
    print(e)

# Essaie d'accéder à __size (ça va échouer aussi)
try:
    print(my_square.__size)
except Exception as e:
    print(e)
