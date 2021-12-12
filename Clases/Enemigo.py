from Mario import Mario
import pyxel
class Enemigo():
    def __init__(self, x, y):
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

    def mover(self, mario: Mario):
        self.__x = self.__x + self.vx
        if mario.x >= (192 / 2) and pyxel.btn(pyxel.KEY_D):
          self.__vx = -1.4


