"""
Puede que la creación de una instancia resulte compleja, o que consuma mucho tiempo.
Para resolver este problema, el patrón de diseño por prototipo permite reemplazar el modelo
de instanciación por la creación de una primera instancia y el clonado posterior de ésta
para las demás creaciones de otras instancias.

Hay que tener en mente que la noción de clonado es propia de cada lenguaje y está prevista,
originalmente, para resolver problemas particulares.

SOLUCIÓN: la solución se realiza en dos etapas. La primera consiste en crear la primera instancia
y la segunda consiste en crear un método de clonado eficaz y sin pérdida de datos.

"""


class A:
    pass


class NoPrototipo:
    def __init__(self):  # método complejo de creación
        self.a = 42
        self.b = 'Complejo'
        self.c = A()
        self.c.a = [1, 2, 3]
        self.c.b = A()
        self.c.b.a = (1, 2, 3)

    def __str__(self):
        return f'{self.a} {self.b} {self.c.a} {self.c.b.a}'
    
a = NoPrototipo()

print(a)

"""
He aquí como implementar el patrón de diseño por prototipo sobre este objeto.

"""

from copy import deepcopy

class Prototipo:
    _instance_reference = None
    
    def __new__(cls):
        if cls._instance_reference is not None:
            print('Clonando...')
            result = object.__new__(cls)
            result.__dict__ = deepcopy(cls._instance_reference.__dict__)
            return result
    
    def __init__(self):
        if self._instance_reference is None:
            return 
        self._instance_reference = None
        
        print('Inicialización...')
    
        # método complejo de creación
    
        self.a = 42
        self.b = 'Complejo'
        self.c = A()
        self.c.a = [1, 2, 3]
        self.c.b = A()
        self.c.b.a = (1, 2, 3)

    def __str__(self):
        return f'{self.a} {self.b} {self.c.a} {self.c.b.a}'

    @property
    def instance_reference(self):
        return self._instance_reference


"""
La idea principal de la solución técnica implementada es almacenar únicamente la instancia 
de referencia en el atributo de clase, aunque este atributo esté vacío para cada instancia, 
de modo que no referencien a la primera de ellas. 
    
El método de creación de la clase realizará, la primera vez, el proceso de creación clásico
y guardará una referencia a la instancia creada. 
    
A continuación, las siguientes veces, se creará un objeto, pero duplicando su contenido a 
partir de la primera instancia. 
    
"""

b = Prototipo()

print(b)

"""
La clase posee una referencia hacia esa instancia, aunque la propia instancia no hace referencia hacia ella.

"""
print(Prototipo.instance_reference)

"""
Se crea un segundo objeto, pero se clona a partir de la primera instancia.

"""
c = Prototipo()

print(c)

"""
Este se ha clonado, pasa por el método de inicialización, que se invoca automáticamente si el método
de construcción devuelve un objeto del tipo adecuado, aunque la primera línea de este método hace que salga 
de él de forma inmediata. 

"""


    
            
        
    


