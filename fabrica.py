"""
Cuando se dispone de una clase madre abstracta y varias clases hijas,
la clase madre permite recoger y aprovechar comportamientos comunes a
todas las clases hijas.

En los lenguajes tipados, una funcionalidad que resulta útil es la posibilidad de
trabajar potencialmente con objetos declarados como que son del tipo de la clase madre,
de manera que su comportamiento pueda homogeneizarse.

Dicho de otro modo, es una forma de evitar repetir clases tantas veces como
clase hijas existan.

Para ello, se utiliza una fábrica, que recibe como parámetro los datos necesarios
para realizar la construcción del objeto, determinando a partir de ciertos objetos
la clase hija que debe instanciar, crear dicha instancia y devolverla. Esta instancia tendrá
el tipo de la clase madre(véase Polimorfismo en Python).

"""


class A:
    pass


class B:
    pass


def fabrica(param):
    if param % 2 == 0:
        return A
    else:
        return B


    
