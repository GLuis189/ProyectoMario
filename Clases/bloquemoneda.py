from Bloques import Bloque


class BloqueRompibleMoneda(Bloque):  # Esta subclase tiene los atributos de los bloques con moneda
    def __init__(self, x, y):
        if not isinstance(x, int):
            raise TypeError("x debe ser un objeto de tipo entero")
        if not isinstance(y, int):
            raise TypeError("y debe ser un objeto de tipo entero")
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__activo = True

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def activo(self):
        return self.__activo

    def romper(self):
        self.__activo = False

