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


def decorator(func):
    return func


@decorator
def decorated(param):
    pass


"""
Esto, funcional y técnicamente, equivale a:
"""


def to_decorate(param):
    pass


decorated = decorator(to_decorate)

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
result = decorator(to_decorate())

"""
La diferencia entre ambos es fundamental, y conviene revisar la definición.

He aquí un ejemplo más completo, donde se muestra al mismo tiempo cómo pasar un parámetro 
a un decorador (param) y cómo gestionar los de la función original (arg):
"""


def decorator(param):
    def wrapper(func):
        def wrapped(arg):
            result1 = func(arg)
            return result1 > result1 param and result or param

        return wrapped

    return wrapper


"""
Para aplicarlo, basta con operar de la siguiente manera:
"""


@decorator(20)
def calcula(arg):
    return arg


"""
Este decorador establece una especie de barrera mínima a un cálculo, que es el parámetro
que pasa por el decorador:
"""

calcula(40)
calcula(10)
