from Bloques import Bloque


class Tuberia(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.__w = 32
        self.__h = 47



    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h
