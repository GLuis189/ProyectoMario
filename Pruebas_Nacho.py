import pyxel



#class Suelo(Bloque):
#   pass
class Fondo():
    def __init__(self):
        self.fondo_u = 0  # se llaman fondo_u y fondo_v porque en la funcion bltm pide valores de u y de v
        self.fondo_v = 0

        # pass

    def update(self, u, v):
        self.fondo_u = u
        self.fondo_v = v

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
        self.__w = 14
        self.__h = 16
        self.__vy = 0
        self.__vx = 0
        self.__q1 = 2
        self.__q2 = 98

        self.__is_alive = True
        self.__Super_Mario = False
        self.__Mario_Fuego = False

    def update(self):
        # Hay que hacer lo del visor para que a la izq se pare
        # Al pulsar A o <- el mario se mueve a la izq
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.__x = max(0, self.__x - 2)
            self.__vx = -1
            self.__q1 = 18
            self.__q2 = 98
            if self.__w > 0:
                self.__w = -self.__w
           # if self.__vx < 0:
            #    self.__w = -self.__w


        else:

            self.__vx = 0
            #self.__q1 = 2
            #self.__q2 = 98
            #self.__w = self.__w
        # Al pulsar D o -> el mario se mueve a la derecha hasta la mitad de la pantalla
        # Con self.__x if 128//2 == self.__x - self.__w hago que no se mueva si esta en la mitad
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):

            self.__x = self.__x = self.__x if 192 // 2 == self.__x - self.__w else max(0, self.__x + 2)
            self.__vx = 1
            self.__q1 = 18
            self.__q2 = 98
            if self.__w < 0:
                self.__w = -self.__w
        else:
            self.__vx = 0
            #self.__q1 = 2
            #self.__q2 = 98
        # Al pulsar el espacio el mario salta
        if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.KEY_UP) and self.__y - self.__vy * 5 <= 50:
            if self.__y - self.__vy * 5 > 10:  #esto dice que solo puedas saltar si la diferencia entre tu posicion y lo q vas a saltar no sea mas grande que x, para que no puedas saltar hasta el infinito
                self.__vy = 1
                self.__y -= self.__vy * 5  # la velocidad a la que salta
                self.__q1 = 2
                self.__q2 = 79
        else:
            self.__vy = 0
            self.__q1 = 2
            self.__q2 = 98
        #if self.__y > 64:
         #   self.__vy = 1
          #  self.__y -= self.__vy * 2  # la velocidad a la que salta



        #if self.__y == 112 - 16:  # con esto el mario deja de tener gravedad a la altura del suelo y asi no sigue bajando hasta la mitad del bloque
        #    self.__y = self.__y
        #else:
        self.__y += self.__vy + 1


    def colisionarArriba(self, x):
        self.__y = x - self.__h
        self.__vy = 0

    def colisionarAbajo(self, x):
        self.__y = x + self.__h


    def draw(self):
        pyxel.blt(self.__x,
                  self.__y,
                  0,
                  self.__q1,
                  self.__q2,
                  self.__w,
                  self.__h,
                  12)

class Bloque():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__w = 16
        self.__h = 16
        self.__is_activo = True


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

    # No tiene mucho sentido este draw asiq si eso lo borramos luego
    #def draw(self):
     #   pyxel.blt(self.__x, self.__y, 0, 0, 62, self.__w, self.__h)

    def update(self, x, y):
        if self.__is_activo:
            self.__x = x
            self.__y = y


class Enemigos():
    pass


class Poderes():
    pass


class App():
    def __init__(self):
        pyxel.init(192, 128, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60)
        pyxel.load("mario_assets.pyxres")
        self.Suelo = self.__crear_suelo(20)  # Con esta función creas el suelo
        self.Mario = Mario()

        self.fondo = Fondo()  # llamamos a la clase fondo
        self.fondo.fondo_u = 2
        self.fondo.fondo_v = 4
        self.bloque = Bloque(30, 60)
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def CrearBLoques(self):
        bloques = []
        for i in range():
            pass
    # Se crea una lista llenas de los bloques q conforman el suelo

    def __crear_suelo(self, num_suelo):
        bloques = []
        for i in range(num_suelo):
            bloques.append(Bloque(16 * i, 128 - 16))  # Con 16 * i, 128 - 16 consigues que se creen los bloques uno al lado del otro
        return bloques

#Luego crearemos update y draw
    def update(self):

        self.Mario.update()
        if (self.Mario.x + abs(self.Mario.w) >= self.bloque.x and self.Mario.x <= self.bloque.x + self.bloque.w
                and self.Mario.y + self.Mario.h >= self.bloque.y and self.Mario.y <= self.bloque.y + self.bloque.h):

            self.Mario.colisionarArriba(self.bloque.y)

        if (self.Mario.x + abs(self.Mario.w) >= self.bloque.x and self.Mario.x <= self.bloque.x + self.bloque.w
                and self.Mario.y + self.Mario.h >= self.bloque.y and self.Mario.y <= self.bloque.y + self.bloque.h):

            self.Mario.colisionarAbajo(self.bloque.y)

        for item in self.Suelo:
            # item.update(self.Mario)
            if (self.Mario.x + 10 >= item.x and self.Mario.x <= item.x + 11
                    and self.Mario.y + 16 >= item.y and self.Mario.y <= item.y + 8):

                self.Mario.colisionarArriba(item.y)

        #for item in self.Suelo:
         #   item.update(self.Mario)

        while self.Mario.x >= (192 / 2) and pyxel.btn(pyxel.KEY_D):  # esto es pues que el fondo solo avance si el mario esta en la mitad de la pantalla

            Bloque.update(self.bloque, self.bloque.x-0.7, self.bloque.y)
            for item in self.Suelo:
                item.update(item.x - 0.7, item.y)
                                                                # esto se va a la funcion update de la clase fondo de arriba y le cambia el valor de x. Cuanto mas grande mas rapido avanzas
            break  # me he dado cuenta q algo hago mal con los while pq me peta el juego, si pongo un break no asique no se

    def draw(self):
        pyxel.cls(6)

        self.Mario.draw()
        pyxel.blt(self.bloque.x, self.bloque.y, 0, 0, 62, 16, 16, 12)
        #Hay que dibujar los bloques y así se dibujan ya q estan dentro de una lista
        for item in self.Suelo:
            pyxel.blt(item.x, item.y, 0, 0, 227, item.w, item.h, 12)
        #pyxel.bltm(0, 0, 0, self.fondo.fondo_u, self.fondo.fondo_v, 7, 2, 12)  # esta funcion bltm se refiere al tilemap para dibujar el fondo pero no se como va. para q se vea q se mueve poner blt
App()