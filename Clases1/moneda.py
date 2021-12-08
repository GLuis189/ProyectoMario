import pyxel

from Clases1.mario import Mario


class Moneda():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__w = 10
        self.__h = 14
        self.__is_active = True

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @property
    def is_active(self):
        return self.__is_active

    def update_moneda(self, mario: Mario):
        if self.__is_active:
            if mario.y == self.__y and mario.x == self.__x:
                mario.tocar_moneda()
                self.__is_active = False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 2, 29, self.__w, self.__h, 12)


