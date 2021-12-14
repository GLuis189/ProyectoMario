from Bloques import Bloque


class BloqueIrrompible(Bloque):  # Esta subclase de la superclase Bloque tiene los atributos de los bloques irrompibles
    def __init__(self, x, y):
        super().__init__(x, y)
        if not isinstance(x, int):
            raise TypeError("x debe ser un objeto de tipo entero")
        if not isinstance(y, int):
            raise TypeError("y debe ser un objeto de tipo entero")
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
