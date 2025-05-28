def inherits_from(obj, a_class):
    """True si obj hérite (directement ou indirectement) de a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
