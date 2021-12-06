

class Poderes():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__is_active = True
        self.__tipo = None

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
