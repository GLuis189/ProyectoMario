

class Poderes():
    def __init__(self, x, y, ):
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__tipo = 0
        self.__is_active = True

        self.__sx = 0
        self.__sy = 45

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

'''
    def update(self, mario: Mario):
        if mario.Super_Mario:
            self.__tipo = 1


    def tocar_mario(self, mario: Mario):
        if self.__tipo == 0:
          mario.tocar_poder(0)
        else:
            mario.tocar_poder(1)
'''



