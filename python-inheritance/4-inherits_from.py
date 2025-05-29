def inherits_from(obj, a_class):
    """
    Retourne True si obj est instance d'une classe héritée (directement ou non)
    de a_class, mais pas si obj est directement une instance de a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
