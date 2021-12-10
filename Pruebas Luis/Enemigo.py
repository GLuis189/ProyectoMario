
class Enemigo():
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

    def mover(self):
        self.__x = self.x + self.vx




