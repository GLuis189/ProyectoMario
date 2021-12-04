import pyxel
from bloque import Bloque

class Mario():
    def __init__(self):
       self.__reset()

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def vy(self):
        return self.__vy

    def __reset(self):
        self.__x = 0
        self.__y = 30
        self.__w = 14
        self.__h = 16
        self.__vy = -1
        self.__vx = 0
        self.__is_alive = True
        self.__Super_Mario = False
        self.__Mario_Fuego = False

    def update(self):
        # Hay que hacer lo del visor para que a la izq se pare
        # Al pulsar A o <- el mario se mueve a la izq
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.__x = max(0, self.__x - 2)

        # Al pulsar D o -> el mario se mueve a la derecha hasta la mitad de la pantalla
        # Con self.__x if 128//2 == self.__x - self.__w hago que no se mueva si esta en la mitad
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.__x = self.__x if 128//2 == self.__x - self.__w else max(0, self.__x + 2)

        self.__y -= self.__vy


    def colisionar(self, bloque: Bloque):
        self.__y -= bloque.y + bloque.h
        self.__vy = 0


    def draw(self):
        pyxel.blt(self.__x, self.__y, 0, 2, 98, self.__w, self.__h, 12)