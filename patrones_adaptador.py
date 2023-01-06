"""
Para disponer procesamientos genéricos, cuando se diseña una arquitectura,
resulta ideal trabajar con una solución que permita disponer de una interfaz común
y crear objetos que vayan a proveer, a continuación, la misma interfaz.

Pocas veces se trabaja únicamente con objetos que hayamos diseñado nosotros mismos,
pues lo habitual es con librerías de terceros, o con objetos diseñados previamente y que
se han adaptado a una problemática diferente a la nuestra.

En cualquier caso, no es posible recuperar estos objetos y meterlos en un molde que
satisfaga directamente nuestras necesidades.

En este caso, la solución más difundida es crear adaptadores, que adaptarán el comportamiento de los
objetos a una interfaz única.

SOLUCIÓN: He aquí un ejemplo de clases que están perfectamente adaptadas a un uso que queremos recuperar,
pero utilizándolas de manera genérica.

"""


class Perro:
    def ladrar(self):
        print("Guau")


class Gato:
    def maullar(self):
        print("Miau")


class Caballo:
    def relinchar(self):
        print("Heeeee")


class Cerdo:
    def grunir(self):
        print("Oink")


"""
Queremos hacer hablar a estos animales de forma genérica. He aquí una
clase que responde de la manera adecuada:

"""

import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def hacerRuido(self):
        return


"""
Podríamos retomar cada una de las cuatro clases anteriores y reescribirlas con el primer método, 
pero esto supondría una pérdida a nivel semántico, aunque sí es potencialmente para otros usos. 

Python proporciona varias soluciones. Una de las más comunes consiste en usar simplemente la 
herencia múltiple. Ofrece una respuesta simple y eficaz sobrecargando el método abstracto para
dirigirlo al método adecuado:

"""


class PerroAlternativo(Animal, Perro):
    def hacerRuido(self):
        return self.ladrar()


"""
Esto podría llevarse a cabo de manera más sencilla (haciendo que el método sea un atributo)

"""


class GatoAlternativo(Animal, Gato):
    hacerRuido = Gato.maullar


# type: ignore
"""
Esto funciona, aunque no se corresponde con el patrón de diseño Adaptador, que podríamos 
aproximar de la siguiente manera:

"""


class CaballoAlternativo(Animal):  # adaptador genérico
    def __init__(self, caballo):
        self.caballo = caballo

    def hacerRuido(self):
        return self.caballo.relinchar()

    def __getattr__(self, attr):
        return self.caballo.__getattr__(attr)


"""
He aquí un adaptador que no hereda de nada y que simplemente redirecciona el método, 
en Python puede escribirse únicamente con el método __getattr__

"""


class CerdoAdaptador:
    def __init__(self, cerdo):
        self.cerdo = cerdo

    def __getattr__(self, attr):
        if attr == 'hacerRuido':
            return self.cerdo.grunir
        return self.getattr(self.cerdo, attr)


"""
He aquí el uso sucesivo de estas clases, con las dos alternativas y los dos adaptadores
(cabe destacar las diferencias en el proceso de instanciación):

"""

for animal in (PerroAlternativo(), GatoAlternativo(), CaballoAlternativo(Caballo()), CerdoAdaptador(Cerdo())):
    animal.hacerRuido()

"""
El adaptador puede verse como un componente que permite, como su propio nombre indica, 
adaptar el componente existente a una interfaz impuesta que difiere. No obstante, a nivel puramente 
técnico, resulta útil cuando se utiliza en colaboración con una fábrica, 
pues esta última puede seleccionar de qué manera decide adaptar una clase. 
De este modo, el proceso de adaptación puede operarse no directamente en tiempo de instanciación, 
sino bajo demanda, cuando se necesita.

"""


def animal_adapterFactory(context):
    if isinstance(context, Perro):
        return PerroAlternativo()
    elif isinstance(context, Gato):
        return GatoAlternativo()
    elif isinstance(context, Caballo):
        return CaballoAlternativo()
    elif isinstance(context, Cerdo):
        return CerdoAdaptador(context)


