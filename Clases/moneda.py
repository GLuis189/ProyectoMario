class Moneda():
    def __init__(self, x, y):
        if not isinstance(x, int):
            raise TypeError("x debe ser un objeto de tipo entero")
        if not isinstance(y, int):
            raise TypeError("y debe ser un objeto de tipo entero")
        self.__x = x
        self.__y = y
        self.__w = 10
        self.__h = 14
        self.__is_active = True

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
    def is_active(self):
        return self.__is_active

    def update(self, x, y):
        if not isinstance(x, float):
            raise TypeError("x debe ser un objeto de tipo flotante")
        if not isinstance(y, int):
            raise TypeError("y debe ser un objeto de tipo entero")
        if self.__is_active:
            self.__x = x
            self.__y = y

    def CogerMoneda(self):
        self.__is_active = False

    def aparecer(self):
        self.__is_active = True


