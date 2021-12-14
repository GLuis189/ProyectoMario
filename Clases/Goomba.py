from Enemigo import Enemigo
from Mario import Mario
import pyxel
class Goomba(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.__w = 16
        self.__h = 16
        self.__sprite_x = 32
        self.__sprite_y = 0
        self.__is_alive = True

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
    def is_alive(self):
        return self.__is_alive

    def morir(self):
        self.__is_alive = False

    def update(self, mario: Mario):
        if abs(mario.x - self.x) <= 192:
            Goomba.mover1(self, mario)

            # Animación del Goomba cambiando de pie al moverse
            if pyxel.frame_count % 30 == 0:
                self.__w = -self.__w

'''
        if (mario.x - self.x) < (mario.y - self.y):
            if (mario.x + abs(mario.w) >= self.x and mario.x <= self.x + self.w
                    and mario.y + mario.h >= self.y and mario.y <= self.y + self.h):
                mario.perdervida()

        if mario.y > self.y:
            if (mario.x + abs(mario.w) >= self.x and mario.x <= self.x + self.w
                    and mario.y + mario.h >= self.y and mario.y <= self.y + self.h):
          ºº      mario.matarenemigo()
                '''