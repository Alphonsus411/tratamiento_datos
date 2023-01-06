"""
Cuando se busca una manera de formalizar cierto número de patrones de inicialización
de un objeto potencialmente complejo, donde la idea consiste en no manipular el objeto directamente,
sino pasando por alguno de sus métodos formalizados.

Cada uno de estos métodos se denomina constructor, el objeto creado, producto,
y el objeto u objetos susceptibles de usar el constructor para recuperar el producto y utilizarlo,
directores.

Los distintos métodos de inicialización de un producto pueden definirse mediante una clase
que tenga como clase madre una clase abstracta. En este caso, hablamos de constructor para la
clase madre y constructor concreto para la clase hija.

La ventaja que ofrece este método es que separa con claridad o aisle el producto del director,
es decir, el objeto utilizado de aquel que lo emplea, obligando a emplear un método predefinido para
iniciar el producto.

SOLUCIÓN: el producto puede generarse mediante una instanciación con muchos parámetros,
y dada la potencia de Python para el paso de parámetros, las posibles soluciones son numerosas.

Lo que propone el patrón de diseño es externalizar los métodos de agrupación y crearlos en las clases
que forman los constructores.

La problemática consiste, además, en aislar el producto del director. El siguiente ejemplo muestra cómo
usar las propiedades, en lugar de los atributos y funciones, lo que permite una manera de controlar los accesos
y las modificaciones, y también evitar complicar la declaración usando métodos como get o set.

"""

import abc


class Producto:

    @property
    def forma(self):
        return self._forma

    @forma.setter
    def forma(self, forma):
        self._forma = forma

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return "Forma: " + self.forma + " Color: " + self.color


"""
He aquí la clase constructor abstracto que se encarga de crear el producto. 
A diferencia de la clase fábrica, donde se pretende generar clases diferentes en función de
los parámetros recibidos, quí se crea una única clase, siempre la misma, parametrizándola de 
forma diferente. La clase abstracta incluye, de manera lógica, el método de creación del producto, 
aunque delega a sus clases hijas su parametrización. 

"""


class Constructor:

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self, producto):
        self._producto = producto

    def crearProducto(self):
        self.producto = Producto()

    @abc.abstractmethod
    def configurarForma(self):
        return

    @abc.abstractmethod
    def configurarColor(self):
        return


class ConstructorCuboAzul(Constructor):
    def configurarForma(self):
        self.producto.forma = "Cubo"

    def configurarColor(self):
        self.producto.color = "Azul"


class ConstructorEsferaRoja(Constructor):
    def configurarForma(self):
        self.producto.forma = "Esfera"

    def configurarColor(self):
        self.producto.color = "Roja"


class ConstructorPiramideVerde(Constructor):
    def configurarForma(self):
        self.producto.forma = "Pirámide"

    def configurarColor(self):
        self.producto.color = "Verde"


"""
El director estará vinculado con un constructor que es un atributo e incluirá un método
para tener en cuenta todo el procedimiento de creación/parametrización en un único método

"""


class Director:
    def __init__(self):
        self._constructor = None

    @property
    def constructor(self):
        return self._constructor

    @constructor.setter
    def constructor(self, constructor):
        self._constructor = constructor

    def configurarProducto(self):
        self.constructor.crearProducto()
        self.constructor.configurarForma()
        self.constructor.configurarColor()


"""
Para utilizar esta clase, hay que instanciar el director, a continuación agregarle el constructor, 
y por último, ejecutar el método de creación/parametrización
"""

director = Director()
director.constructor = ConstructorPiramideVerde()
director.configurarProducto()

print(director.constructor.producto)
