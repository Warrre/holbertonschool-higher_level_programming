class MyList(list):
    """Classe qui hérite de list avec affichage trié"""
    def print_sorted(self):
        print(sorted(self))
