import pyxel


class Fondo:
    def __init__(self,x ,y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Montana(Fondo):
    def __init__(self, x, y):
        super().__init__(x, y)


class Nube(Fondo):
    def __init__(self, x, y):
        super().__init__(x, y)
