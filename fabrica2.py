"""
El modelo de datos de Python, al ser tan completo,
permite ir mas allá con el concepto de fábrica, es decir,
integrar la fábrica directamente en el núcleo del proceso de creación de la clase madre.

Instanciamos un objeto de la clase madre, obteniendo un objeto de la clase hija
correspondiente, seleccionada de manera determinista.
Esto puede llevarse a cabo correctamente, puesto que el método de discriminación
de las clases hijas lo incluye la clase madre, quien decide en función de un parámetro
que precisa cada una de las clases hijas.

La inicialización de la clase está centrada en la clase madre, puesto que es común

"""

import abc
import os.path


class Loader(metaclass=abc.ABCMeta):
    def __new__(cls, filename):
        ext = os.path.splitext(filename)[-1]

        for sub in cls.__subclasses__():
            if sub.isDesignedFor(ext):
                o = object.__new__(sub)
                o.__init__(filename)
                return o

    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def isDesignedFor(cls, ext):
        if ext in cls.extensions:
            return True
        return False

    @abc.abstractmethod
    def load(self):
        return


class TextLoader(Loader):
    extensions = ['.txt']

    def load(self):
        print('Archivo de Texto')


#        with open(self.filename) as f:
#           return f.readlines()

import csv


class CSVLoader(Loader):
    extensions = ['.csv']

    def load(self):
        print('Archivo CSV')


#     with open(self.filename) as f:
#          return csv.reader(f.read())

import pickle


class PickLoader(Loader):
    extensions = ['.pckl']

    def load(self, filename):
        print('Archivo Pickle')

#      with open(self.filename) as f:
#            return pickle.load(f)
