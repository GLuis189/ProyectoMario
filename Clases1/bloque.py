import pyxel
from Clases1.mario import Mario

class Bloque():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__is_activo = True
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def is_activo(self):
        return self.__is_activo


    # No tiene mucho sentido este draw asiq si eso lo borramos luego
    def draw(self):
        pyxel.blt(self.__x, self.__y, 0, 0, 62, self.__w, self.__h)


class Suelo(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 16
        self.__h = 16
        self.__is_activo = True

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    def update(self, mario: Mario):
        if self.is_activo:
            if mario.y == self.y:
                mario.colisionar()

class Incognita(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 17
        self.__h = 16

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

