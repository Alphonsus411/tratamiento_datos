"""
El objetivo de un decorador es agregar dinámicamente funcionalidades,
haciéndolo por composición en lugar de por herencia.

El concepto se expresa, matemáticamente, como "círculo". De este modo, la expresión matemática
(decorador o función)(params) puede, también, expresarse en informática por la función
decorador (función)(params).

Un decorador, es, por tanto, una función que transforma una función en otra función,
o incluso una función que transforma una clase en otra clase.

La problemática consiste en gestionar la manera en la que se componen las funcionalidades,
y su resolución no es trivial en un lenguaje clásico. Pero no para Phyton, dado el hecho de que
todo es un objeto, incluso las clases y las funciones.

Los decoradores son, por tanto, una alternativa compleja, aunque seductora. Por este motivo,
se han convertido en un elemento esencial del lenguaje e incluso disponen de una síntaxis propia
para aplicarlos.

SOLUCIÓN: He aquí un ejemplo muy sencillo con un decorador identidad(devuelve la función
que recibe como parámetro) y un decorado:
"""
import functools


def Decorator(func):
    return func


@Decorator
def Decorated(param):
    pass


"""
Esto, funcional y técnicamente, equivale a:
"""


def To_Decorate(param):
    pass


Decorated = Decorator(To_Decorate)

"""
De este modo, cuando se realiza una llamada a la función decorada tal y como se ha declarado antes, 
se produce lo equivalente a:
"""

# result = decorated("value")

"""
No es exactamente esto:
"""
# result = decorated(decorator(to_decorate("value")))

"""
Sino más bien:
"""
# result = decorator(to_decorate())

"""
La diferencia entre ambos es fundamental, y conviene revisar la definición.

He aquí un ejemplo más completo, donde se muestra al mismo tiempo cómo pasar un parámetro 
a un decorador (param) y cómo gestionar los de la función original (arg):
"""


def Decorator(param):
    def Wrapper(func):
        def Wrapped(arg):
            result1 = func(arg)
            return result1 > param and result1 or param

        return Wrapped

    return Wrapper


"""
Para aplicarlo, basta con operar de la siguiente manera:
"""


@Decorator(20)
def calcula(arg):
    return arg


"""
Este decorador establece una especie de barrera mínima a un cálculo, que es el parámetro
que pasa por el decorador:
"""

calcula(40)
calcula(10)

"""
La decoración de una función es una operación que modifica en profundidad la función, incluidos sus metadatos. 
Normalmente, cuando se tiene una función, se tiene lo siguiente:
"""


def Ejemplo():
    """ Ejemplo Docstring"""
    """ Ejemplo docstring"""

    Ejemplo.__name__

    Ejemplo.__doc__


"""
He aquí lo que ocurre cuando se decora la función:
"""


def My_Decorator(f):
    """  Decorador Docstring"""

    def Wrapper(*args, **kwargs):
        """ Wrapper Docstring"""
        return f(*args, **kwargs)

    return Wrapper


@My_Decorator
def Ejemplo():
    """ Ejemplo Docstring"""
    """ Ejemplo Docstring"""
    Ejemplo.__name__

    Ejemplo.__doc__


"""
He aquí una solución que permite que la función decorada se parezca a la original:
"""


def My_Decorator(f):
    """ Decorador Docstring"""

    @functools.wraps(f)
    def Wrapper(*args, **kwargs):
        """ Wrapper Docstring"""
        return f(*args, **kwargs)

    return Wrapper


@My_Decorator
def Ejemplo():
    """ Ejemplo Docstring"""
    Ejemplo.__name__

    Ejemplo.__doc__


"""
CONCLUSIONES:

Dominar la creación de decoradores supone conocer perfectamente el modelo de objetos de Python 
y basarse en su propia experiencia para comprender y experimentar el ámbito completo de 
aplicación de este concepto. Por el contrario, el uso de un decorador, es, en Python, la solución que 
permite responder a muchos casos de uso, dado que es extremadamente eficaz. 

Se utiliza, por otro lado, en funcionalidades tan importantes como la transformación de métodos 
para hacerlos estáticos o de clase. A lo largo del repositorio veremos varios tipos de decoradores y sus 
distintas aplicaciones. 
"""


