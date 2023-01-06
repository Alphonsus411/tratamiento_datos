"""
Un singletown, es en matemáticas, un conjunto que posee un solo elemento.
En informática, se trata de una clase que posee una única instancia.

"""


class Singletown:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            return cls.instance


# object() is object(), Singletown is Singletown()
# (False, True)



