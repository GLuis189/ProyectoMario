from Bloques import Bloque

class BloqueInterrogacion(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        activo = True
        Poder = 0
