class Poderes():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__tipo = 0
        self.__is_active = True
        self.__sprite_x = 0
        self.__sprite_y = 45

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

    def update(self):
        self.__is_active = False