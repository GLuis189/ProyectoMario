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

class Goomba(Enemigos):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 15
        self.__h = 15

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    def update(self):
        self.__x = max(0, self.__x - 2)


