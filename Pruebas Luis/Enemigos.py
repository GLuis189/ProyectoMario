class Enemigos(object):
    def __init__(self, posicion_x, posicion_y, velocidad_x, vivo):
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y
        self.Velocidad_X = velocidad_x
        self.Vivo = vivo

class Goomba(Enemigos):
    def __init__(self, posicion_x, posicion_y, velocidad_x):
        super().__init__(posicion_x, posicion_y, velocidad_x)
        self.Velocidad_X = self.mover()

    def mover(self):
        self.Velocidad_X = -2

class Koopa_Troopa(Enemigos):
    def __init__(self, posicion_x, posicion_y, velocidad_x, concha):
        super().__init__(posicion_x, posicion_y, velocidad_x)
        self.Concha = concha
