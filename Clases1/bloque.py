
from Clases1.mario import Mario

class Bloque():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__is_activo = True

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def is_activo(self):
        return self.__is_activo

    def update(self, mario: Mario):
        if self.__is_activo:
            if mario.y == self.__y:
                 mario.colisionar_arriba(self.__y)

class Suelo(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 16
        self.__h = 16
        self.__sprite_x = 0
        self.__sprite_y = 227

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



class Incognita(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 17
        self.__h = 16
        self.__sprite_x = 176
        self.__sprite_y = 27

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

'''
    Hay que hacer que cuando el bloque lo toque mario por abajo salga el poder y se ejecute el update
    def update(self):
        if not self.is_activo:
            self.__w = 17
            self.__sprite_x = 144
            self.__sprite_y = 27
'''

class Ladrillo_Rompible(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 16
        self.__h = 16
        self.__sprite_x = 152
        self.__sprite_y = 200

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


class Ladrillo_Irrompible(Bloque):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__w = 16
        self.__h = 16
        self.__sprite_x = 152
        self.__sprite_y = 200

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