class MyList(list):
    """Classe qui hérite de list avec une méthode pour afficher la liste triée."""
    
    def print_sorted(self):
        """Affiche la liste triée en ordre croissant."""
        print(sorted(self))
