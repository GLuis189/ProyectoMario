from Mario import Mario
from Bloques import Bloque
from BloqueIrrompible import BloqueIrrompible
from tuberia import  Tuberia
from interrogacion import BloqueInterrogacion
from BloqueIrrompible import BloqueIrrompible
from Poderes import Poderes
import pyxel
class Draw():
    def DrawMario(self, Mario: Mario):
        pyxel.blt(Mario.x,
                  Mario.y,
                  0,
                  Mario.q1,
                  Mario.q2,
                  Mario.w,
                  Mario.h,
                  12)
    def DrawBloquesSuelo(self, Bloques: Bloque):
        pyxel.blt(Bloques.x, Bloques.y, 0, 0, 227, Bloques.w, Bloques.h, 12)

    def DrawTuberias(self, tuberia: Tuberia):
        pyxel.blt(tuberia.x, tuberia.y, 0, 79, 178, tuberia.w, tuberia.h, 12)

    def DrawBloquesIrrompibles(self, BloqueIrrompible: BloqueIrrompible):
        pyxel.blt(BloqueIrrompible.x, BloqueIrrompible.y, 0, 0, 62, BloqueIrrompible.w, BloqueIrrompible.h, 12)

    def DrawBloqueInterrogacion(self, interrogacion: BloqueInterrogacion):
        pyxel.blt(interrogacion.x, interrogacion.y, 0, 177, 27, interrogacion.w, interrogacion.h, 12)

    def DrawBLoqueRompible(self, BloqueRompible: Bloque):
        pyxel.blt(BloqueRompible.x, BloqueRompible.y, 0, 160, 200, BloqueRompible.w, BloqueRompible.h, 12)

    def DrawPoderes(self, Poderes: Poderes):
        pyxel.blt(Poderes.x, Poderes.y, 0, Poderes.sprite_x, Poderes.sprite_y, Poderes.w, Poderes.h, 12)

    def DrawScore(self, score):
        pyxel.text(4, 4, score, 7)

    def DrawMonedas(self, monedas):
        pyxel.blt(50, 2, 0, 81, 16, 5, 8, 12)
        pyxel.text(56, 4, monedas, 7)
