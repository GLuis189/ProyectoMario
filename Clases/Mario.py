import pyxel


class Mario():
    def __init__(self, posicion_x: int, posicion_y: int, velocidad_x, velocidad_y, vidas, Vivo=True) -> None:
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y
        self.Velocidad_X = velocidad_x
        self.Velocidad_Y = velocidad_y
        self.Vidas = vidas
        self.Morir = Vivo

    def mover(self):
        self.Posicion_X += self.Velocidad_X
        self.Posicion_Y -= self.Velocidad_Y

    def Update(self):
        pass



    def Draw(self):
        pyxel.blt(self.Posicion_X, self.Posicion_Y, 0, 2, 98, 13, 15)






