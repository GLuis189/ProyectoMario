from Bloques import Bloque


class Tuberia(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.__w = 31
        self.__h = 47

    def draw(self):
        pyxel.blt(self.__x, self.__y, 0, 79, 178, 31, 47, 12)