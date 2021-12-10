from Enemigo import Enemigo

class Goomba(Enemigo):
    def __init__(self, posicion_x, posicion_y):
        super().__init__(posicion_x, posicion_y)
        self.Velocidad_X = self.mover()

    def mover(self):
        self.Velocidad_X = -2
