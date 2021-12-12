import pyxel


class Mario():
    def __init__(self):
        self.__reset()
        self.__Vidas = 3
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

    @property
    def q1(self):
        return self.__q1

    @property
    def q2(self):
        return self.__q2

    @property
    def score(self):
        return self.__score

    @property
    def monedas(self):
        return self.__monedas

    @property
    def Vidas(self):
        return self.__Vidas

    @property
    def Reset(self):
        return self.__reset()

    @property
    def Mario_Fuego(self):
        return self.__Mario_Fuego

    @property
    def ganar(self):
        return self.__Ganar

    def __reset(self):
        self.__x = 20
        self.__y = 80
        self.__w = 15
        self.__h = 16
        self.__vy = 1
        self.__q1 = 2
        self.__q2 = 98
        self.__score = 0
        self.__monedas = 0
        self.encimadebloque = False
        self.Supermario = False
        self.__is_alive = True
        self.__Mario_Fuego = False
        self.__Ganar = False


    def update(self):
        # Hay que hacer lo del visor para que a la izq se pare
        # Al pulsar A o <- el mario se mueve a la izq
        if self.Supermario == True:
            self.__w = 16
            self.__h = 32
            self.__q1 = 54
            self.__q2 = 82
        if self.__Mario_Fuego == True:
            self.Supermario = False
            self.__w = 16
            self.__h = 32
            self.__q1 = 169
            self.__q2 = 81
        if not self.__Ganar:
            if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
                self.__x = max(0, self.__x - 2)
                if self.__w > 0:
                    self.__w = -self.__w
                if pyxel.frame_count % 30 < 15 and not pyxel.btn(pyxel.KEY_SPACE):
                    if not self.Supermario or not self.__Mario_Fuego:
                        self.__q1 = 18
                        self.__q2 = 98

                    if self.Supermario:
                        self.__q1 = 88
                        self.__q2 = 82

                    if self.__Mario_Fuego:
                        self.__q1 = 39
                        self.__q2 = 135

                else:
                    if not self.Supermario or not self.__Mario_Fuego:
                        self.__q1 = 0
                        self.__q2 = 98

                    if self.Supermario:
                        self.__q1 = 105
                        self.__q2 = 82
                    if self.__Mario_Fuego:
                        self.__q1 = 122
                        self.__q2 = 195




            # Al pulsar D o -> el mario se mueve a la derecha hasta la mitad de la pantalla

            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):

                self.__x = self.__x if 96 == self.__x - self.__w else min(192 / 2, max(0, self.__x + 2))

                if self.__w < 0:
                    self.__w = -self.__w
                if pyxel.frame_count % 30 < 15 and not pyxel.btn(pyxel.KEY_SPACE):
                    if not self.Supermario or not self.__Mario_Fuego:
                        self.__q1 = 18
                        self.__q2 = 98

                    if self.Supermario:
                        self.__q1 = 88
                        self.__q2 = 82

                    if self.__Mario_Fuego:
                        self.__q1 = 39
                        self.__q2 = 135

                else:
                    if not self.Supermario or not self.__Mario_Fuego:
                        self.__q1 = 0
                        self.__q2 = 98

                    if self.Supermario:
                        self.__q1 = 106
                        self.__q2 = 82

                    if self.__Mario_Fuego:
                        self.__q1 = 122
                        self.__q2 = 195

            # Al pulsar el espacio el mario salta
            if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.KEY_UP):
                #if self.encimadebloque == True:
                    #self.encimadebloque = False
                self.__vy = 5
                self.__y -= self.__vy   # la velocidad a la que salta
                if not self.Supermario or self.__vy > 0 and not self.__Mario_Fuego:
                    self.__q1 = 2
                    self.__q2 = 80

                if self.Supermario:
                    self.__q1 = 146
                    self.__q2 = 80

                if self.__Mario_Fuego:
                    self.__q1 = 67
                    self.__q2 = 136

        if self.__y > 160:
            self.Morir()
            self.__reset()

        self.__vy = 1
        self.__y += self.__vy


    def colisionarArriba(self, x):
        self.__y = x - self.__h
        self.__vy = 0
        self.encimadebloque = True

    def colisionarArribaG(self, x):
        self.__y = x - self.__h
        self.__vy = 0
        self.encimadebloque = True
        self.__score += 10

    def colisionarAbajo(self, x):
        self.__y = x + self.__h

    def colisionarIzq(self, x):
        self.__x = x - self.__w

    def colisionarDrch(self, x):
        self.__x = x + self.__w

    def CogerSeta(self):
        self.Supermario = True
        self.__score += 1000

    def CogerFLor(self):
        self.__Mario_Fuego = True
        self.__score += 1000

    def cogerMoneda(self):
        self.__monedas += 1
        self.__score += 100

    def activarBloqueI(self, x):
        self.colisionarAbajo(x)

    def Morir(self):
        self.__Vidas -= 1


    def Ganar(self, x, y):
        self.__y = y
        self.__x = x
        self.__Ganar = True
        self.__score += 500

    def Final(self):
        if self.__x != 848:
            self.__x = self.__x if 96 == self.__x - self.__w else min(192 / 2, max(0, self.__x + 2))


