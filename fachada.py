"""
El objetivo del patrón de diseño fachada consiste en ocultar la complejidad de un sistema ofreciendo
un objeto simple que permita responder a las problemáticas que necesitan la mayoría de usuarios.

La fachada realiza una especie de interfaz entre el programa principal y un módulo muy complejo.
Sus funcionalidades pueden abarcar las de varios componentes para agruparlas en una misma
fachada.

SOLUCIÓN: En primer lugar, es preciso crear algunas clases que interactúen entre sí para responder
a una funcionalidad. Además, se complican un poco las cosas de cara a apreciar un poco mejor
nuestra fachada:
"""


class Word:
    def hello(self):
        return 'Hello, I\'m'

    def goodbye(self):
        return 'Goodbye, I\'m'


class Speaker:
    def __init__(self, name):
        self.name = name

        @classmethod
        def say(cls, what, to):
            word = Word()
            metodo = getattr(word, what)
            if metodo is None:
                return ' '
            return ' '.join((metodo(), to))

        def speak(self, what):
            return Speaker.say(what, self.name)

        def who(self):
            return self.name


class Dialog:
    def __init__(self, speaker1, speaker2):
        self.speaker1 = Speaker(speaker1)
        self.speaker2 = Speaker(speaker2)
        self.sentences = []

    def __call__(self):
        sentences = []
        sentences.append(self.speaker1.speak('hello'))
        sentences.append(self.speaker2.speak('hello'))
        sentences.extend(self.sentences)
        sentences.append(self.speaker1.speak('goodbye'))
        sentences.append(self.speaker2.speak('goodbye'))
        return '\n'.join(['- %s' % s for s in sentences])


"""
Se tienen, por tanto, tres clases y se pretende proveer una interfaz sencilla a un desarrollador que 
utilizará nuestras clases, donde las dos funcionalidades esenciales son "hacer decir algo a alguien" 
e "iniciar un diálogo" .

He aquí una fachada apropiada:
"""


class Facade:
    @classmethod
    def say(cls, what, to):
        print(Speaker.say(what, to))

    def dialog(self, speaker1, speaker2, sentences):
        dialog = Dialog(speaker1, speaker2)
        dialog.sentences = sentences
        print(dialog())

"""
La fachada respeta las clases que utiliza, y proporciona dos métodos cuyas firmas son más 
sencillas. El primero es una simple redirección hacia un método de otra clase, 
el segundo realiza el trabajo suplementario para que el usuario no tenga que hacerlo. 

He aquí cómo utilizar el primero:
"""

Facade.say('hello', 'World')

"""

"""


