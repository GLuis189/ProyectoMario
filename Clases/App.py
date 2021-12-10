import pyxel
#import random
from Bloques import Bloque
from tuberia import Tuberia
from interrogacion import BloqueInterrogacion
from Mario import Mario
from BloqueIrrompible import BloqueIrrompible
from BloqueRompible import BloqueRompible
from moneda import Moneda
#from Goomba import Goomba
#from KoopaTroopa import KoopaTroopa
from Poderes import Poderes
from Draw import Draw
from Nubes import Nube
from Montanas import Montana

class App():
    def __init__(self):
        pyxel.init(192, 144, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60)
        pyxel.load("mario_assets.pyxres")
        self.Suelo = self.__crear_suelo(56)  # Con esta función creas el suelo
        self.tuberias = self.crearTuberias()
        self.BloquesRompibles = self.crearBloquesRompibles()
        self.BloquesInterrogacion = self.crearInterrogacion()
        self.Mario = Mario()
        self.Dibujar = Draw()
        self.Poderes = self.crearPoderes()
        self.Monedas = self.crearMonedas()
        self.BLoquesIrrompibles = self.crearBloquesIrrompibles()
        self.Enemigos = self.crearEnemigos()
        self.Nubes = self.crearNubes()
        self.Montanas = self.crearMontanas()
        self.time = 300


        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def __crear_suelo(self, num_suelo):  # Se crea una lista llenas de los bloques q conforman el suelo
        bloques = []
        cont = 0
        for i in range(num_suelo):
            cont += 1
            if cont < 16 or cont > 19:
                bloques.append(Bloque(16 * i, 144 - 16))  # Con 16 * i, 128 - 16 consigues que se creen los bloques uno al lado del otro
        return bloques

    def crearBloquesIrrompibles(self):
        bloques = [BloqueIrrompible(192, 112), BloqueIrrompible(208, 112), BloqueIrrompible(224, 112), BloqueIrrompible(208, 96), BloqueIrrompible(224, 96), BloqueIrrompible(224, 80), BloqueIrrompible(304, 112), BloqueIrrompible(704, 112), BloqueIrrompible(704, 96), BloqueIrrompible(704, 80), BloqueIrrompible(688, 64), BloqueIrrompible(704, 64)]
        return bloques
    def crearTuberias(self):
        bloques = [Tuberia(432, 112), Tuberia(544, 82)]
        return bloques
    def crearBloquesRompibles(self):
        bloques = [BloqueRompible(112, 64), BloqueRompible(128, 64), BloqueRompible(352, 80), BloqueRompible(368, 80), BloqueRompible(384, 80), BloqueRompible(352, 26), BloqueRompible(624, 80), BloqueRompible(640, 80)]
        return bloques
    def crearInterrogacion(self):
        bloques = [BloqueInterrogacion(166, 64), BloqueInterrogacion(368, 26)]
        return bloques
    def crearMonedas(self):
        monedas = [Moneda(148, 64), Moneda(368, 10), Moneda(352, 10), Moneda(384, 60), Moneda(704, 44), Moneda(685, 108)]
        return monedas
    def crearPoderes(self):  # con esto se crean los poderes como la seta o la flor
        poderes = []
        for item in range(len(self.BloquesInterrogacion)):
            if self.BloquesInterrogacion[item].recompensa:
                poderes.append(Poderes(self.BloquesInterrogacion[item].x, self.BloquesInterrogacion[item].y - 16, 0))  # esto hace q la seta o el poder aparezca encima
                poderes[item].aparecer()  # este metodo de poderes pone en true el self.__is_active para q se pueda dibujar la seta

        return poderes
    def crearEnemigos(self):
        enemigos = []
        return enemigos
    def crearNubes(self):
        nubes = [Nube(10, 32), Nube(180, 16), Nube(270, 32), Nube(340, 26)]
        return nubes
    def crearMontanas(self):
        montana = [Montana(0,0), Montana(0,0), Montana(0,0)]
        return montana

#Luego crearemos update y draw
    def update(self):

        self.Mario.update()

        # coger Poderes
        for item in self.Poderes:
            if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                    and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                self.Poderes.remove(item)
                self.Mario.CogerPoder()
        #coger moneda
        for item in self.Monedas:
            if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                    and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                self.Mario.cogerMoneda()
                self.Monedas.remove(item)
                item.CogerMoneda()
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
                    item.romper()


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
            for item in self.Monedas:
                item.update(item.x - 1, item.y)
            for item in self.Poderes:
                item.update(item.x - 1, item.y)
            for item in self.Nubes:
                item.update(item.x - 1, item.y)

            break  # me he dado cuenta q algo hago mal con los while pq me peta el juego, si pongo un break no asique no se
        self.time += 1
    def draw(self):
        pyxel.cls(6)

        #  Hay que dibujar los bloques y así se dibujan ya q estan dentro de una lista
        for item in self.Nubes:
            self.Dibujar.DrawNube(item)
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
        for item in self.Monedas:
            if Moneda.is_active:
                self.Dibujar.DrawMoneda(item)
        for item in self.Poderes:
            if item.is_activo:
                self.Dibujar.DrawPoderes(item)

        #for item in self.Montanas:
         #   self.Dibujar.DrawMontana(item)

        self.Dibujar.DrawMario(self.Mario)

        s = "MARIO\n{:>0000006}".format(self.Mario.score)
        self.Dibujar.DrawScore(s)
        m = "X {:>02}".format(self.Mario.monedas)
        self.Dibujar.DrawMonedas(m)
        self.Dibujar.DrawMundo()
        t = "TIME\n {:<300}".format(self.time)
        self.Dibujar.DrawTime(t)


App()
