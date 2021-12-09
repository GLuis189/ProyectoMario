import pyxel


class Mario():
    def __init__(self):
       self.__reset()

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def vy(self):
        return self.__vy

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h


    def __reset(self):
        self.__x = 20
        self.__y = 64
        self.__w = 15
        self.__h = 16
        self.__vy = 1
        self.__vx = 0
        self.__q1 = 2
        self.__q2 = 98
        self.encimadebloque = False
        self.Supermario = False

        self.__is_alive = True
        self.__Super_Mario = False
        self.__Mario_Fuego = False

    def update(self):
        # Hay que hacer lo del visor para que a la izq se pare
        # Al pulsar A o <- el mario se mueve a la izq
        if self.Supermario == True:
            self.__w = 16
            self.__h = 32
            self.__q1 = 54
            self.__q2 = 82
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.__x = max(0, self.__x - 2)
            self.__vx = 1
            if self.__vx > 0 and not self.Supermario:
                self.__q1 = 18
                self.__q2 = 98
            elif self.__vx > 0 and self.Supermario:
                self.__q1 = 88
                self.__q2 = 82
            if self.__w > 0:
                self.__w = -self.__w
        else:
            self.__vx = 0


        # Al pulsar D o -> el mario se mueve a la derecha hasta la mitad de la pantalla

        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):

            self.__x = self.__x if 96 == self.__x - self.__w else min(192 / 2, max(0, self.__x + 2))
            self.__vx = 1
            if self.__vx > 0 and not self.Supermario:
                self.__q1 = 18
                self.__q2 = 98

            if self.__vx > 0 and self.Supermario:
                self.__q1 = 88
                self.__q2 = 82
            else:
                self.__q1 = 18
                self.__q2 = 98
            if self.__w < 0:
                self.__w = -self.__w
            if self.__vx == 0 and not self.Supermario:
                self.__q1 = 0
                self.__q2 = 98
        else:
            self.__vx = 0
        # Al pulsar el espacio el mario salta
        if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.KEY_UP):
            #if self.encimadebloque == True:
                #self.encimadebloque = False
            self.__vy = 1
            self.__y -= self.__vy * 5  # la velocidad a la que salta
            if self.__vy > 0 and not self.Supermario:
                self.__q1 = 2
                self.__q2 = 80

            elif self.__vy > 0 and self.Supermario:
                self.__q1 = 146
                self.__q2 = 80
        else:
            self.__vy = 0


        self.__vy = 1
        self.__y += self.__vy


    def colisionarArriba(self, x):
        self.__y = x - self.__h
        self.__vy = 0
        self.encimadebloque = True

    def colisionarAbajo(self, x):
        self.__y = x + self.__h

    def colisionarIzq(self, x):
        self.__x = x - self.__w

    def colisionarDrch(self, x):
        self.__x = x + self.__w

    def CogerSeta(self):
        self.Supermario = True

    def activarinterrogacion(self):
        activo = True


    def draw(self):
        pyxel.blt(self.__x,
                  self.__y,
                  0,
                  self.__q1,
                  self.__q2,
                  self.__w,
                  self.__h,
                  12)





