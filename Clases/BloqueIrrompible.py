from Bloques import Bloque


class BloqueIrrompible(Bloque):  # Esta subclase de la superclase Bloque tiene los atributos de los bloques irrompibles
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
