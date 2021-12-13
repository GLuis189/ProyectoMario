from Bloques import Bloque


class BloqueRompible(Bloque):  # Esta subclase de la superclase Bloque tiene los atributos de los bloques rompibles
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__activo = True

    def romper(self):  # Este metodo define mediante un booleano si el bloque ya esta roto
        self.__activo = False
