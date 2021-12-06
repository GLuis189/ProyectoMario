class Enemigos():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__vx = -1
        self.__is_alive = True
        self.__puntos = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def vx(self):
        return self.__vx

# Hacer los setter para poder modificar la velocidad

    def mover(self):
        self.__x = self.x + self.vx


class Goomba(Enemigos):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 16
        self.__h = 16
        self.__sprite_x = 0
        self.__sprite_y = 0

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

    def update(self):
       Goomba.mover(self)

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

    def update(self):
        pass



