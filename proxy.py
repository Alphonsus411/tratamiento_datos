"""
El patrón de diseño Proxy o delegado es una clase que sustituye a otra presentando exactamente
las mismas características externas,
o una parte, y redirige sus métodos a esta o modifica el resultado.

SOLUCIÓN: la solución, que permite crear un proxy identidad, es la siguiente:
"""


class IdentityProxy:
    def __init__(self, context):
        self.context = context

    def __getattr__(self, name):
        return getattr(self.context, name)


"""
Este proxy puede utilizarse para proyectar un punto del espacio sobre un plano horizontal.
He aquí el punto:
"""


class Punto:
    def __init__(self, x, y, z):
        self._x, self._y, self._z = x, y, z

    def x(self):
        return str(self._x)

    def y(self):
        return str(self._y)

    def z(self):
        return str(self._z)


"""
He auí la proyección(heredando del Proxy, el contexto es ahora el punto del espacio):
"""


class Proyeccion(IdentityProxy):
    def z(self):
        return '0'


"""
He aquí una función que permite visualizar el resultado en forma de 3 tuplas:
"""


def formateador(punto):
    return '(%s)' % ', '.join((punto.x(), punto.y(), punto.z()))


"""
He aquí como construir nuestros puntos:
"""

punto = Punto(1, 2, 3)
proyeccion = Proyeccion(punto)

"""
Y mostrarlos:
"""

print(formateador(punto))

print(formateador(proyeccion))

"""
Mas allá del contexto genérico, es posible crear un proxy a medida para presentar únicamente el método
o los métodos que se quiere mostrar, omitiendo los demás. 
Para ello existen varios medios. El más sencillo, el que se muestra a continuación:
"""


class A:
    def m1(self):
        pass

    def m2(self):
        pass

    def m3(self):
        pass


"""
A continuación, el proxy, que define, el mismo, su contexto y que opera la redirección 
de métodos hacia el contexto:
"""


class ProxyDeA:
    def __init__(self):
        self.context = A()

    def m1(self):
        return self.context.m1()

    def m3(self):
        return self.context.m3()


"""
He aquí las diferencias entre ambos:
"""

a1 = A()
'm1' in dir(a1), 'm2' in dir(a1)

a2 = ProxyDeA()
'm1' in dir(a2), 'm2' in dir(a2)

"""
He aquí una clase Proxy más genérica:
"""


class ProxySelectivo:
    redirected = ['m1', 'm3']

    def __init__(self, context):
        self.context = context

    def __getattr__(self, name):
        if name in self.redirected:
            return setattr(self.context, name)

"""
Los métodos redirigidos no son visibles para dir, aunque están presentes:
"""

a3 = ProxySelectivo(A())
'm1' in dir(a3), 'm2' in dir(a3)
a3.m1, a3.m2

"""
CONCLUSIONES: el Proxy es muy sencillo de implementar y permite simplificar la apariencia de un objeto. 
Por el contrario, es posible diseñar objetos muy complejos que permitan gestionar más casos de uso, 
y, a continuación, construir un proxy por cada caso de uso. 
"""

