from Mario import Mario
from Bloques import Bloque
from BloqueIrrompible import BloqueIrrompible
from tuberia import  Tuberia
from interrogacion import BloqueInterrogacion
from BloqueIrrompible import BloqueIrrompible
from Poderes import Poderes
from moneda import Moneda
from Nubes import Nube
from Montanas import Montana
from meta import Meta
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
        if interrogacion.activo:
            pyxel.blt(interrogacion.x, interrogacion.y, 0, 177, 27, interrogacion.w, interrogacion.h, 12)
        elif not interrogacion.activo:
            pyxel.blt(interrogacion.x, interrogacion.y, 0, 145, 27, interrogacion.w, interrogacion.h, 12)

    def DrawBLoqueRompible(self, BloqueRompible: Bloque):
        pyxel.blt(BloqueRompible.x, BloqueRompible.y, 0, 160, 200, BloqueRompible.w, BloqueRompible.h, 12)

    def DrawPoderes(self, Poderes: Poderes):
        if Poderes.is_activo:
            pyxel.blt(Poderes.x, Poderes.y, 0, Poderes.sprite_x, Poderes.sprite_y, Poderes.w, Poderes.h, 12)

    def DrawScore(self, score):
        pyxel.text(4, 4, score, 7)

    def DrawMonedas(self, monedas):
        pyxel.blt(50, 2, 0, 81, 16, 5, 8, 12)
        pyxel.text(56, 4, monedas, 7)

    def DrawMundo(self):
        pyxel.text(100, 4, "WORLD\n 1-1", 7)

    def DrawVidas(self, vidas):
        pyxel.text(180, 130, vidas, 7)

    def DrawTime(self, time):
        pyxel.text(150, 4, time, 7)

    def DrawMoneda(self, moneda: Moneda):
        pyxel.blt(moneda.x, moneda.y, 0, 2, 29, moneda.w, moneda.h, 12)

    def DrawNube(self, nube: Nube):
        pyxel.blt(nube.x, nube.y, 0, 108, 139, 46, 21, 12)

    def DrawMontana(self, montana: Montana):
        pyxel.blt(montana.x, montana.y, 0, 0, 181, 75, 45, 12)

    def DrawMeta(self, meta: Meta):
        pyxel.blt(meta.x, meta.y, 0, 233, 121, meta.w, meta.h, 12)
        pyxel.blt(meta.x + 16, meta.y + 14, 0, 155, 134, 74, 92, 12)
    def DrawGameOver(self):
        pyxel.cls(0)
        pyxel.text(77, 63, "GAME OVER" , 8)
        pyxel.text(74, 63, "\n \n Pulsa q \n para cerrar ", 7)


