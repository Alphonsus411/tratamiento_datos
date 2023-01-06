"""
El puente es un patrón de diseño que tiene como objetivo desacoplar la interfaz de implementación,
lo que permite fusionar las funcionalidades de dos tipos de clases de jerarquías ortogonales.
Por ejemplo, dados los tres tipos de datos:
- Ciudad
- Provincia
- Región

Con dos posibilidades de almacenar o cargar datos:
- CSV
- Pickle

Resulta posible basarse en uno de estos diseños, y a continuación, crear una clase para cada caso
para cada caso de uso que requiera el otro concepto.
Se obtienen, de este modo, seis clases:
- csvCiudades
- csvProvincias
- csvRegiones
- pickleCiudades
- pickleProvincias
- pickleRegiones

Evidentemente, parte del código de cada clase es redundante respecto a los distintos conceptos.
Python proporciona soluciones, gracias a la herencia múltiple, que permiten definir tres clases
para gestionar el aspecto de los datos relativos a las ciudades, las regiones y las provincias,
y otras dos clases para gestionar el aspecto de carga/registro para CSV y Pickle.
Tan solo queda construir las seis clases que heredan cada una de las combinaciones de los
seis conceptos.

Esta manera de trabajar resulta más sencilla, muy básica, aunque no necesariamente más legible
o con una mejor capacidad de evolución, puesto que si agrega un concepto o una nueva clase en
algún concepto es preciso crear todas las clases necesarias para tener en cuenta este cambio,
lo cual puede resultar una operación bastante incómoda.

La solución consiste en utilizar el puente que, según la sintaxis de su uso, puede parecerse
vagamente al adaptador, pero que es muy diferente. No se trata de hacer apuntar una semántica a otra,
sino más bien permitir desacoplar varias nociones en el seno de la misma clase.
"""

"""
SOLUCIÓN: He aquí un ejemplo que utiliza los dos conceptos con dos nociones cada uno. El primero 
es relativo a la naturaleza de los datos que se han de cargar:
"""

import abc
import csv
import pickle


class Loader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self):
        return


class CSVLoader(Loader):
    def load(self, filename):
        print('Archivo CSV')
        with open(filename) as f:
            return csv.reader(f.read())


class PickleLoader(Loader):
    def load(self, filename):
        print('Archivo Pickle')
        with open(filename) as f:
            return pickle.load(f)


"""
 Esta primera serie de clases presenta una relación de madre a hija. La clase concreta es la implementación
 abstracta de la interfaz entre el dato almacenado de manera persistente y la del objeto manipulable. 
 Ambos objetos son derivados concretos. La segunda serie de clases son los puentes, 
 que permiten tratar los datos abstrayendo su procedencia, pero aplicando la 
 misma transformación:
 """


class Transformer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def transform(self):
        return


"""
El método loadDatos, es, por tanto, un método dependiente de la implementación,
es decir, de las tres clases Loader; de ahí que sea de bajo nivel. El método depende 
únicamente de su clase abstracta, por lo que decimos que es de alto nivel.
"""


class UpperTransformer(Transformer):
    def __init__(self, filename, loader):
        self.filename = filename
        self.loader = loader

    def loadDatos(self):
        self.content = self.loader.load(self.filename)
        # En caso de que haya comentarios en el loader
        if self.content is None:
            self.content = [['Chisme', 'algo'],
                            ['cOsA', 'TRASTO']]

    def transform(self):
        for i, l in enumerate(self.content):
            for j, d in enumerate(l):
                self.content[i][j] = d.upper()


class LowerTransformer(Transformer):
    def __init__(self, filename, loader):
        self.filename = filename
        self.loader = loader

    def loadDatos(self):
        self.content = self.loader.load(self.filename)
        # En caso de que haya comentarios en el loader
        if self.content is None:
            self.content = [
                ['Chisme', 'algo'],
                ['cOsA', 'TRASTO']]

    def transform(self):
        for i, l in enumerate(self.content):
            for j, d in enumerate(l):
                self.content[i][j] = d.lower()


"""
He aquí como utilizar este puente:
"""
test1 = UpperTransformer('test.csv', loader=CSVLoader())

"""
El componente de implementación se pasa como parámetro. 
Tan sólo queda usar los métodos. El de bajo nivel:
"""

test1.loadDatos()

"""
Y el de alto nivel:
"""
test1.transform()

"""
También es posible ver a qué se parecen los datos así procesados:
"""
test1.content()

"""
He aquí el uso de los mismos componentes en otro contexto:
"""
test2 = LowerTransformer('test.pkl', loader=PickleLoader())
test2.loadDatos()

test2.transform()

test2.content()

"""
Conclusiones:

Dado que en Python es todo un objeto, y que una clase o una función son, 
ellas mismas objetos, existen soluciones mucho más sencillas que consisten en 
pasar la propia clase como parámetro a un método, por ejemplo. Las opciones que ofrece 
la arquitectura son relativamente numerosas. Resulta preferente, en este caso, 
la creación de componentes autónomos, perfectamente desacoplados, y vinculados 
entre sí en una segunda etapa, en lugar de crear uno e introducir la noción de bajo y alto nivel, 
donde uno utiliza al otro. 

Las soluciones que emplea la herencia múltiple pueden resultar, en algunos casos, 
ventajosas, aunque no son las preferentes. 
"""
