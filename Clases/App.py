import pyxel
#import random
from Bloques import Bloque
from tuberia import Tuberia
from interrogacion import BloqueInterrogacion
from Mario import Mario
from BloqueIrrompible import BloqueIrrompible
from BloqueRompible import BloqueRompible
#from Enemigos import Enemigos
from Poderes import Poderes
from Draw import Draw

class App():
    def __init__(self):
        pyxel.init(192, 128, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60)
        pyxel.load("mario_assets.pyxres")
        self.Suelo = self.__crear_suelo(56)  # Con esta función creas el suelo
        self.tuberias = self.crearTuberias()
        self.BloquesRompibles = self.crearBloquesRompibles()
        self.BloquesInterrogacion = self.crearInterrogacion()
        self.Mario = Mario()
        self.Dibujar = Draw()
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
        bloques = [BloqueIrrompible(192, 96), BloqueIrrompible(208, 96), BloqueIrrompible(224, 96), BloqueIrrompible(208, 80), BloqueIrrompible(224, 80), BloqueIrrompible(224, 64), BloqueIrrompible(304, 96), BloqueIrrompible(704, 96), BloqueIrrompible(704, 80), BloqueIrrompible(704, 64), BloqueIrrompible(688, 48), BloqueIrrompible(704, 48)]
        return bloques
    def crearTuberias(self):
        bloques = [Tuberia(432, 96), Tuberia(544, 66)]
        return bloques
    def crearBloquesRompibles(self):
        bloques = [BloqueRompible(112, 48), BloqueRompible(128, 48), BloqueRompible(352, 64), BloqueRompible(368, 64), BloqueRompible(384, 64), BloqueRompible(352, 10), BloqueRompible(624, 64), BloqueRompible(640, 64)]
        return bloques
    def crearInterrogacion(self):
        bloques = [BloqueInterrogacion(166, 48), BloqueInterrogacion(368, 10)]
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

        self.Dibujar.drawMario(self.Mario)
        if self.Seta.is_activo:
            self.Dibujar.DrawPoderes(self.Seta)

        #  Hay que dibujar los bloques y así se dibujan ya q estan dentro de una lista
        for item in self.BloquesRompibles:
            self.Dibujar.DrawBLoqueRompible(item)
        for item in self.BloquesInterrogacion:
            self.Dibujar.DrawBloqueInterrogacion(item)
        for item in self.BLoquesIrrompibles:
            self.Dibujar.DrawBloquesIrrompibles(item)
        for item in self.tuberias:
            self.Dibujar.DrawTuberias(item)
        for item in self.Suelo:
            self.Dibujar.DrawBloquesSuelo(item)

App()