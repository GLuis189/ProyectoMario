from Enemigo import Enemigo
import pyxel
from Mario import Mario

class Koopa_Troopa(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        if not isinstance(x, int):
            raise TypeError("x debe ser un objeto de tipo entero")
        if not isinstance(y, int):
            raise TypeError("y debe ser un objeto de tipo entero")

        self.__w = 15
        self.__h = 23
        self.__sprite_x = 32
        self.__sprite_y = 0
        self.__is_alive = True

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @property
    def sprite_x(self):
        return self.__sprite_x

    @property
    def sprite_y(self):
        return self.__sprite_y

    @property
    def is_alive(self):
        return self.__is_alive

    def morir(self):
        self.__is_alive = False

    def update(self, mario: Mario):
        if not isinstance(mario, Mario):
            raise TypeError("mario debe ser un objeto de tipo Mario")

        if abs(mario.x - self.x) <= 192:
            Koopa_Troopa.mover2(self, mario)
            if pyxel.frame_count % 30 == 0:
                self.__w = -self.__w
