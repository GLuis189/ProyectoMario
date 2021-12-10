import pyxel

from Mario import Mario
from Enemigo import Enemigo

class Goomba(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 16
        self.__h = 16
        self.__sprite_x = 32
        self.__sprite_y = 0

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

    def update(self, mario: Mario):
        if abs(mario.x - self.x) <= 192:
            Goomba.mover(self)
            if pyxel.frame_count % 30 == 0:
                self.__w = -self.__w

