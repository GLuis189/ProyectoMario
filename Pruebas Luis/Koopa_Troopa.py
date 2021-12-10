from Clases1.enemigos import Enemigos


class Koopa_Troopa(Enemigos):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 16
        self.__h = 24
        self.__sprite_x = 0
        self.__sprite_y = 24

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @property
    def sprite_x(self):
        return self.__sprite_x

    @property
    def sprite_y(self):
        return self.__sprite_y


