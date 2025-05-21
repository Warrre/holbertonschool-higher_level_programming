class Square:
    def __init__(self, size=0):
        self.size = size  # Utilise le setter

    @property
    def size(self):
        """Getter pour la taille."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter avec vérifications."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
