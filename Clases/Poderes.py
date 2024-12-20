class Poderes():
    def __init__(self, x, y, tipo):
        if not isinstance(x, float):
            raise TypeError("x debe ser un objeto de tipo flotante")
        if not isinstance(y, int):
            raise TypeError("y debe ser un objeto de tipo entero")
        if not isinstance(tipo, int):
            raise TypeError("tipo debe ser un objeto de tipo entero")
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__tipo = tipo
        self.__is_active = False
        if self.__tipo == 0:
            self.__sprite_x = 0
            self.__sprite_y = 45
        elif self.__tipo == 1:
            self.__sprite_x = 55
            self.__sprite_y = 47

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
    def sprite_x(self):
        return self.__sprite_x

    @property
    def sprite_y(self):
        return self.__sprite_y

    @property
    def is_activo(self):
        return self.__is_active

    @property
    def tipo(self):
        return self.__tipo

    def coger(self):
        self.__is_active = False

    def aparecer(self):
        self.__is_active = True

    def update(self, x, y):
        if not isinstance(x, float):
            raise TypeError("x debe ser un objeto de tipo flotante")
        if not isinstance(y, int):
            raise TypeError("y debe ser un objeto de tipo entero")
        self.__x = x
        self.__y = y