"""
E objeto "Composite" es un patrón de diseño que tiene como objetivo construir un tronco común
a varios objetos similares para permitir realizar una manipulación genérica de dichos objetos.

El componente es la clase abstracta de todo componente, el composite es un componente que puede
contener otros, a diferencia de la hoja, que es el final.

SOLUCIÓN: la solución, con Phyton, consiste en utilizar simplemente una clase abstracta que contenga
los métodos comunes y sobrecargar los métodos en el composite y en la hoja,

Estos dos objetos, por sí solos, permiten representar el árbol.

He aquí un componente que posee un único método que le permite describirse:
"""

import abc


class Componente(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def verbose(self, level=0):
        return


"""
La hoja sobrecarga el método abstracto:
"""


class Hoja(Componente):
    def verbose(self, level=0):
        return '%s Hoja %s' % ('\t' * level, self.name)


"""
El componente también, aunque añade elementos secundarios:
"""


class Composite(Componente):
    def __init__(self, name):
        Componente.__init__(self, name)
        self.contenido = []

    def add(self, componente):
        self.contenido.append(componente)

    def verbose(self, level=0):
        hojas = [f.verbose(level +1) for f in self.contenido]
        hojas.insert(0, '%s Composite %s' % ('\t' * level, self.name))
        return '\n'.join(hojas)

"""
He aquí la clase cliente, que utiliza nuestro patrón de diseño. Empezamos creando dos hojas:
"""

c1 = Hoja("H1")
c2 = Hoja("H2")

"""
A continuación, un composite:
"""
c3 = Composite("C1")

""""
Al que es posible agregar hojas:
"""
c3.add(Hoja("H4"))
c3.add(Hoja("H5"))
c3.add(Hoja("H6"))

"""
También es posible crear un composite al que se agregan otros composites:
"""

c4 = Composite("C2")
c41 = Composite("C3")

"""
Para ir más rápido, se agrega directamente los composites modificando el atributo que 
los contiene:
"""
c41.contenido = [Hoja("H7"), Hoja("H8"), Hoja("H9")]
c4.contenido = [Composite("C4"), c41, Hoja("HA")]

"""
Es posible, en cada etapa de la creación, verificar lo que responde el método de descripción. 
También es posible agruparlo todo sobre la misma raíz:
"""

main = Composite('Test')
main.contenido.extend([c1, c2, c3, c4])

"""
Se obtiene:
"""
print(main.verbose())








