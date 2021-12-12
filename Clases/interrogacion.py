from Bloques import Bloque
from Poderes import Poderes
class BloqueInterrogacion(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__activo = True
        self.__recompensa = False


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
    def activo(self):
        return self.__activo

    @property
    def recompensa(self):
        return self.__recompensa

    def update(self, x, y):

        self.__x = x
        self.__y = y

    def romper(self):
        self.__activo = False
        self.__recompensa = True


