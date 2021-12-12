import pyxel
#import random
#from Bloques import Bloque
#from tuberia import Tuberia
#from interrogacion import BloqueInterrogacion
from Mario import Mario
#from BloqueIrrompible import BloqueIrrompible
#from BloqueRompible import BloqueRompible
from moneda import Moneda
#from Goomba import Goomba
#from KoopaTroopa import KoopaTroopa
from Poderes import Poderes
from Draw import Draw
#from Nubes import Nube
#from Montanas import Montana
from meta import Meta
#from bloquemoneda import BloqueRompibleMoneda
from Creador import Creador

class App():
    def __init__(self):
        pyxel.init(192, 144, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60)
        pyxel.load("mario_assets.pyxres")
        self.Crear = Creador()
        self.Suelo = self.Crear.crear_suelo(64)  # Con esta función creas el suelo
        self.tuberias = self.Crear.crearTuberias()
        self.BloquesRompibles = self.Crear.crearBloquesRompibles()
        self.BloquesInterrogacion = self.Crear.crearInterrogacion()
        self.Mario = Mario()
        self.Dibujar = Draw()
        self.Poderes = self.crearPoderes()
        self.Monedas = self.Crear.crearMonedas()
        self.BLoquesIrrompibles = self.Crear.crearBloquesIrrompibles()
        self.Enemigos = self.Crear.crearEnemigos()
        self.Bloquesmoneda = self.Crear.crearBloquesconmoneda()
        self.Nubes = self.Crear.crearNubes()
        self.Montanas = self.Crear.crearMontanas()
        self.Meta = Meta(832, 23)
        self.time = 300
        self.GameOver = False
        self.Lista = list(self.Suelo + self.tuberias + self.BloquesRompibles
                          + self.BloquesInterrogacion + self.Monedas + self.BLoquesIrrompibles + self.Enemigos
                          + self.Poderes + self.Bloquesmoneda + self.Nubes + self.Montanas)

        pyxel.run(self.update, self.draw)


    def crearPoderes(self):  # con esto se crean los poderes como la seta o la flor
        poderes = []
        for item in range(len(self.BloquesInterrogacion)):
            if self.BloquesInterrogacion[item].recompensa and not self.BloquesInterrogacion[item].activo:
                poderes.append(Poderes(self.BloquesInterrogacion[item].x, self.BloquesInterrogacion[item].y - 16, 1 if self.Mario.Supermario else 0))  # esto hace q la seta o el poder aparezca encima
                for poder in range(len(poderes)):
                    poderes[poder].aparecer()  # este metodo de poderes pone en true el self.__is_active para q se pueda dibujar la seta
        return poderes



#Luego crearemos update y draw
    def update(self):

        self.Mario.update()

        # coger Poderes
        for item in self.Poderes:
            if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                    and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                self.Poderes.remove(item)
                if item.tipo == 0:
                    self.Mario.CogerSeta()
                elif item.tipo == 1:
                    self.Mario.CogerFLor()
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
                    if self.Mario.Supermario or self.Mario.Mario_Fuego:
                        item.romper()
                        self.BloquesRompibles.remove(item)
        for item in self.Bloquesmoneda:
            # colision por arriba con los bloques rompibles
            cont = 0
            if self.Mario.y < item.y:
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarArriba(item.y)
            # colision por abajo con los bloques rompibles
            elif self.Mario.y > item.y:
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarAbajo(item.y)
                    self.Monedas.append(Moneda(item.x, item.y - 20))
                    cont += 1
                    if self.Mario.Supermario or self.Mario.Mario_Fuego:

                        #if cont >= 4:
                            item.romper()
                            self.Bloquesmoneda.remove(item)

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
                    self.Poderes = self.crearPoderes()

        for item in self.tuberias:
            # colision por arriba con los tuberias
            if (self.Mario.x - item.x) < (self.Mario.y - item.y):
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarIzq(item.x)
            elif (self.Mario.x - item.x) < (self.Mario.y - item.y):
                if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                        and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                    self.Mario.colisionarDrch(item.x + item.w)
            else:
                if self.Mario.y < item.y:
                    if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                            and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                        self.Mario.colisionarArriba(item.y)
                # colision por abajo con los bloques irrompibles
                elif self.Mario.y > item.y:
                    if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                            and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                        self.Mario.colisionarAbajo(item.y)

        # llegar a la meta
        if (self.Mario.x + abs(self.Mario.w) >= self.Meta.x and self.Mario.x <= self.Meta.x + self.Meta.w
                and self.Mario.y + self.Mario.h >= self.Meta.y and self.Mario.y <= self.Meta.y + self.Meta.h):
            if self.time % 5 == 0:
                self.Mario.Ganar(self.Meta.x, self.Meta.y)
            self.Mario.Final()

        # colision con el suelo
        for item in self.Suelo:
            if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                    and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):

                self.Mario.colisionarArriba(item.y)

        # esto es para que el fondo solo avance si el mario esta en la mitad de la pantalla y está pulsando D o ->
        if self.Mario.x >= (192 / 2) and pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            for item in self.Lista:
                item.update(item.x - 1.4, item.y)
            for item in self.Poderes:
                item.update(item.x - 1.4, item.y)
            self.Meta.update()

        # El tiempo se va reduciedo cada vez que pasa 1 segundo (fps%60=0) y si el tiempo se acaba se pierde.
        if self.time > 0:
            if pyxel.frame_count % 60 == 0:
                self.time -= 1
        else:
            self.GameOver = True

        # Si Mario pierde las vidas se pierde.
        if self.Mario.Vidas <= 0:
            self.GameOver = True

    def draw(self):
        pyxel.cls(6)

        # Llamamos a las funciones de dibujar dentro de la clase Draw.
        for item in self.Nubes:
            self.Dibujar.DrawNube(item)
        for item in self.Montanas:
            self.Dibujar.DrawMontana(item)
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
        for item in self.Bloquesmoneda:
            if item.activo:
                self.Dibujar.DrawBLoqueRompible(item)
        for item in self.Poderes:
            if item.is_activo:
                self.Dibujar.DrawPoderes(item)

        self.Dibujar.DrawMeta(self.Meta)
        self.Dibujar.DrawMario(self.Mario)
        v = "X {}".format(self.Mario.Vidas)
        self.Dibujar.DrawVidas(v)
        s = "MARIO\n{:>0000006}".format(self.Mario.score)
        self.Dibujar.DrawScore(s)
        m = "X {:>02}".format(self.Mario.monedas)
        self.Dibujar.DrawMonedas(m)
        self.Dibujar.DrawMundo()
        t = "TIME\n {}".format(self.time)
        self.Dibujar.DrawTime(t)

        if self.GameOver:
            self.Dibujar.DrawGameOver()


App()
