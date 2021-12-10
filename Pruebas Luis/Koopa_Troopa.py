from Enemigo import Enemigo


class Koopa_Troopa(Enemigo):
    def __init__(self, posicion_x, posicion_y, velocidad_x, concha):
        super().__init__(posicion_x, posicion_y, velocidad_x)
        self.Concha = concha