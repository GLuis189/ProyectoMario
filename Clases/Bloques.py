import pyxel

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
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h


    # No tiene mucho sentido este draw asiq si eso lo borramos luego
    #def draw(self):
     #   pyxel.blt(self.__x, self.__y, 0, 0, 62, self.__w, self.__h)

    def update(self, x, y):
        if self.__is_activo:
            self.__x = x
            self.__y = y






