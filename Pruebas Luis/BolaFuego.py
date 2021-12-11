from Mario import  Mario
import pyxel

class BolaFuego():
    def __init__(self, mario: Mario):
        self.__x = mario.x + mario.w
        self.__y = mario.y + mario.h/2
        self.__w = 8
        self.__h = 8
        self.__q1 = 32
        self.__q2 = 323
        self.__is_activo = False
        self.__rebotes = False
        self.__direc = 0

    def update(self, x, y):
        if self.__is_activo:
            self.__x = x
            self.__y = y

    def generarBola(self, mario: Mario):
        if mario.Mario_Fuego:
            if pyxel.btnp(pyxel.KEY_F):
                self.__is_activo = True


    def rebotar(self, x, y):
        if self.__is_activo:
            self.__x = max(0, self.__x + 3) * -1 ** self.__direc
            self.__y = max(0, self.__y + 1)
