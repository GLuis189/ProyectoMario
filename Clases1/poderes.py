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

    def update(self, mario: Mario):
        if mario.Super_Mario:
            self.__tipo = 1

    def tocar_mario(self, mario: Mario):
        if (
            mario.x + abs(mario.w) >= self.__x
            and mario.x <= self.__x + self.__w
            and mario.y - mario.h >= self.__y
            and mario.y <= self.__y + self.__h
        ):
            if self.__tipo == 0:
              mario.tocar_poder(0)
            else:
                mario.tocar_poder(1)




