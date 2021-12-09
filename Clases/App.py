import pyxel
#import random
from Bloques import Bloque
from tuberia import Tuberia
from interrogacion import BloqueInterrogacion
from Mario import Mario
#from Enemigos import Enemigos
from Poderes import Poderes
class App():
    def __init__(self):
        pyxel.init(192, 128, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60)
        pyxel.load("mario_assets.pyxres")
        self.Suelo = self.__crear_suelo(56)  # Con esta función creas el suelo
        self.tuberias = self.crearTuberias()
        self.BloquesRompibles = self.crearBloquesRompibles()
        self.BloquesInterrogacion = self.crearInterrogacion()
        self.Mario = Mario()
        self.Seta = Poderes(100, 60)
        self.BLoquesIrrompibles = self.crearBloquesIrrompibles()



        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def __crear_suelo(self, num_suelo):  # Se crea una lista llenas de los bloques q conforman el suelo
        bloques = []
        cont = 0
        for i in range(num_suelo):
            cont += 1
            if cont < 16 or cont > 19:
                bloques.append(Bloque(16 * i, 128 - 16))  # Con 16 * i, 128 - 16 consigues que se creen los bloques uno al lado del otro
        return bloques

    def crearBloquesIrrompibles(self):
        bloques = [Bloque(192, 96), Bloque(208, 96), Bloque(224, 96), Bloque(208, 80), Bloque(224, 80), Bloque(224, 64), Bloque(304, 96), Bloque(704, 96), Bloque(704, 80), Bloque(704, 64), Bloque(688, 48), Bloque(704, 48)]
        return bloques
    def crearTuberias(self):
        bloques = [Tuberia(432, 96), Tuberia(544, 66)]
        return bloques
    def crearBloquesRompibles(self):
        bloques = [Bloque(112, 48), Bloque(128, 48), Bloque(352, 64), Bloque(368, 64), Bloque(384, 64), Bloque(352, 10), Bloque(624, 64), Bloque(640, 64)]
        return bloques
    def crearInterrogacion(self):
        bloques = [Bloque(166, 48), Bloque(368, 10)]
        return bloques

#Luego crearemos update y draw
    def update(self):

        self.Mario.update()

        # coger Seta

        if (self.Mario.x + abs(self.Mario.w) >= self.Seta.x and self.Mario.x <= self.Seta.x + self.Seta.w
                and self.Mario.y + self.Mario.h >= self.Seta.y and self.Mario.y <= self.Seta.y + self.Seta.h):
            self.Seta.update()
            self.Mario.CogerSeta()

        for item in self.BLoquesIrrompibles:
            # colision por arriba con los bloques irompibles

           # if self.Mario.y < item.y:
                #if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                    #    and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    #self.Mario.colisionarArriba(item.y)
            # colision por abajo con los bloques irrompibles
            #elif self.Mario.y > item.y:
                #if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                     #   and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    #self.Mario.colisionarAbajo(item.y)
            if (self.Mario.x - item.x) < (self.Mario.y - item.y):
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarIzq(item.x)
            elif (self.Mario.x - item.x) < (self.Mario.y - item.y):
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarDrch(item.x)

            else:
                if self.Mario.y < item.y:
                    if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                            and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                        self.Mario.colisionarArriba(item.y)
                 #colision por abajo con los bloques irrompibles
                elif self.Mario.y > item.y:
                    if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                            and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                        self.Mario.colisionarAbajo(item.y)



        for item in self.BloquesRompibles:
            # colision por arriba con los bloques rompibles
            if self.Mario.y < item.y:
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarArriba(item.y)
            # colision por abajo con los bloques rompibles
            elif self.Mario.y > item.y:
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarAbajo(item.y)

        for item in self.BloquesInterrogacion:
            # colision por arriba con los bloques interrogacion
            if self.Mario.y < item.y:
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarArriba(item.y)
            # colision por abajo con los bloques interrogacion
            elif self.Mario.y > item.y:
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarAbajo(item.y)

        for item in self.tuberias:
            # colision por arriba con los tuberias
            if self.Mario.y < item.y:
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarArriba(item.y)
            # colision por abajo con los tuberias
            elif self.Mario.y > item.y:
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarAbajo(item.y)

        # colision con el suelo
        for item in self.Suelo:
            # item.update(self.Mario)
            if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                    and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):

                self.Mario.colisionarArriba(item.y)

        #for item in self.Suelo:
         #   item.update(self.Mario)

        while self.Mario.x >= (192 / 2) and pyxel.btn(pyxel.KEY_D):  # esto es pues que el fondo solo avance si el mario esta en la mitad de la pantalla
            for item in self.BloquesRompibles:
                item.update(item.x - 1, item.y)
            for item in self.BloquesInterrogacion:
                item.update(item.x - 1, item.y)
            for item in self.tuberias:
                item.update(item.x - 1, item.y)
            for item in self.Suelo:
                item.update(item.x - 1, item.y)
            for item in self.BLoquesIrrompibles:
                item.update(item.x - 1, item.y)

            break  # me he dado cuenta q algo hago mal con los while pq me peta el juego, si pongo un break no asique no se

    def draw(self):
        pyxel.cls(6)

        self.Mario.draw()
        if self.Seta.is_activo:
            pyxel.blt(self.Seta.x, self.Seta.y, 0, self.Seta.sprite_x, self.Seta.sprite_y, self.Seta.w, self.Seta.h, 12)

        #  Hay que dibujar los bloques y así se dibujan ya q estan dentro de una lista
        for item in self.BloquesRompibles:
            pyxel.blt(item.x, item.y, 0, 160, 200, 16, 16, 12)
        for item in self.BloquesInterrogacion:
            pyxel.blt(item.x, item.y, 0, 177, 27, 16, 16, 12)
        for item in self.BLoquesIrrompibles:
            pyxel.blt(item.x, item.y, 0, 0, 62, 16, 16, 12)
        for item in self.tuberias:
            pyxel.blt(item.x, item.y, 0, 79, 178, 32, 47, 12)
        for item in self.Suelo:
            pyxel.blt(item.x, item.y, 0, 0, 227, item.w, item.h, 12)
        #pyxel.bltm(0, 0, 0, self.fondo.fondo_u, self.fondo.fondo_v, 7, 2, 12)  # esta funcion bltm se refiere al tilemap para dibujar el fondo pero no se como va. para q se vea q se mueve poner blt
App()