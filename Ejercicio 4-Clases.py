import pyxel

class Juego():
    def __init__(self):
        pyxel.init(256, 160, caption="Mario Bross")
        pyxel.run(self.update, self.draw)

#Luego crearemos update y draw y queremos crear una pantalla de título
    def update(self):
       pass
    def draw(self):
        pass
    def update_portada(self):
        pass

class Mario():
    def __init__(self, posicion_x: int, posicion_y: int) -> None:
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y
        self. velocidad = 0
    def mover(self):
        #Presionar Q para q se mueva si no esta mas de la mitad de la pantalla.

class Bloques(object):
    def __init__(self, posicion_x: int, posicion_y: int) -> None:
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y
        self.Rompible = None

class Bloques_Rompibles(Bloques):
    def __init__(self,posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Rompible = True

class Bloques_Irompibles(Bloques):
    def __init__(self,posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Rompible = False









class Poderes():
    def __init__(self):

    class Fuego(poderes)
        def __init__(self):
    class Crecer(poderes)
        def __init__(self):
    class Estrella(poderes)
        def __init__(self):

class Enemigos()
    def __init__(self, ):