from Clases1.mario import Mario


class Moneda():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__w = 10
        self.__h = 14
        self.__is_active = True

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

    def update(self, mario = Mario):
        if self.__is_active:
            if mario.y == self.__y and mario.x == self.__x:
                mario.colisionar()
