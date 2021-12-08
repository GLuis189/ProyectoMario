from Clases1.mario import Mario


class Poder():
    def __init__(self, x, y, ):
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__tipo = 0
        self.__is_active = True
        self.__sprite_x = 0
        self.__sprite_y = 45

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

    @property
    def sprite_x(self):
        return self.__sprite_x

    @property
    def sprite_y(self):
        return self.__sprite_y

    @property
    def is_active(self):
        return self.__is_active

    def update(self, mario: Mario):
        if mario.Super_Mario or mario.Mario_Fuego:
            self.__tipo = 1
        if self.__tipo == 1:
            self.__sprite_x = 55
            self.__sprite_y = 46

    def tocar_mario(self, mario: Mario):
        if self.__tipo == 0:
          mario.tocar_poder(0)
        if self.__tipo == 1:
            mario.tocar_poder(1)
        self.__is_active = False



