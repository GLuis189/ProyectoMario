from Mario import Mario
import pyxel


class Enemigo():
    def __init__(self, x, y):
        if not isinstance(x, int):
            raise TypeError("x debe ser un objeto de tipo entero")
        if not isinstance(y, int):
            raise TypeError("y debe ser un objeto de tipo entero")
        self.__x = x
        self.__y = y
        self.__vx = -1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def vx(self):
        return self.__vx

    def morir(self):
        self.__vx = 0

    def mover1(self, mario: Mario):
        if not isinstance(mario, Mario):
            raise TypeError("mario debe ser un objeto de tipo Mario")
        self.__x = self.__x + (1 * self.__vx)
        if mario.x >= (192 / 2) and pyxel.btn(pyxel.KEY_D):
            self.__vx = -1.2

    def mover2(self, mario: Mario):
        if not isinstance(mario, Mario):
            raise TypeError("mario debe ser un objeto de tipo Mario")
        self.__x = self.__x + (1 * self.__vx)
        if mario.x >= (192 / 2) and pyxel.btn(pyxel.KEY_D):
            self.__vx = -1
