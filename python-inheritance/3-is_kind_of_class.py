def is_kind_of_class(obj, a_class):
    """Retourne True si obj est instance de a_class ou d'une classe héritée de a_class."""
    return isinstance(obj, a_class)
