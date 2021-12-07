import pyxel


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
    def h(self):
        return self.__h

    @property
    def w(self):
        return self.__w

    @property
    def vy(self):
        return self.__vy

    @property
    def Super_Mario(self):
        return self.__Super_Mario

    @property
    def Mario_Fuego(self):
        return self.__Mario_Fuego

    def __reset(self):
        self.__x = 20
        self.__y = 40
        self.__w = 14
        self.__h = 16
        self.__vy = 0

        self.__is_alive = True
        self.__Mini_Mario = True
        self.__Super_Mario = False
        self.__Mario_Fuego = False

        self.__Contador_Monedas = 0
        self.__Puntos = 0

        self.__sprite_x = 2
        self.__sprite_y = 98

    def update(self):
        # Hay que hacer lo del visor para que a la izq se pare
        # Al pulsar A o <- el mario se mueve a la izq
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.__x = max(0, self.__x - 2)
            if self.__w > 0:
                self.__w = -self.__w

        # Al pulsar D o -> el mario se mueve a la derecha hasta la mitad de la pantalla
        # Con self.__x if 128//2 == self.__x - self.__w hago que no se mueva si esta en la mitad
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.__x = self.__x if 192 // 2 == self.__x - self.__w else max(0, self.__x + 2)
            if self.__w < 0:
                self.__w = -self.__w


        # Al pulsar el espacio el mario salta
        if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.KEY_UP) and self.__y - self.__vy * 5 <= 100:
            if self.__y - self.__vy * 5 > 10:
                self.__vy = 1
                self.__y -= self.__vy * 5  # la velocidad a la que salta

         # con esto el mario deja de tener gravedad a la altura del suelo y asi no sigue bajando hasta la mitad del bloque

        self.__y += self.__vy + 1

        if self.__Super_Mario:
            self.super_mario()

        if self.__Mario_Fuego:
            self.mario_fuego()

    def super_mario(self):
        self.__w = 16
        self.__h = 32
        self.__sprite_x = 54
        self.__sprite_y = 82

    def mario_fuego(self):
        self.__w = 14
        self.__h = 31
        self.__sprite_x = 169
        self.__sprite_y = 81

    def colisionar_arriba(self, y_bloque):
        self.__y = y_bloque - self.__h
        self.__vy = 0

    def colisionar_abajo(self, y_bloque):
        self.__y = y_bloque - self.__h

    def tocar_moneda(self):
        self.__Contador_Monedas += 1

    def tocar_poder(self, n):
        if n == 0:
            self.__Mini_Mario = False
            self.__Super_Mario = True
            self.__Mario_Fuego = False

        if n == 1:
            self.__Mini_Mario = False
            self.__Super_Mario = False
            self.__Mario_Fuego = True



    def draw(self):
        if self.__Mini_Mario:
            pyxel.blt(self.__x, self.__y, 0, self.__sprite_x, self.__sprite_y, self.__w, self.__h, 12)
        if self.__Super_Mario:
            pyxel.blt(self.__x, self.__y, 0, self.__sprite_x, self.__sprite_y, self.__w, self.__h, 12)
        if self.__Mario_Fuego:
            pyxel.blt(self.__x, self.__y, self.__sprite_x, self.__sprite_y, self.__w, self.__h, 12)
