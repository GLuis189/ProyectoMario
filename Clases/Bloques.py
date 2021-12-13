

class Bloque():  # Esta es la superclase de la que derivan el resto de clases de bloques
    def __init__(self, x, y):
        self.reset(x, y)


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

    def update(self, x, y):
        self.__x = x
        self.__y = y

    def reset(self, x, y):
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__is_activo = True


