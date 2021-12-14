from Mario import Mario
from Bloques import Bloque
from tuberia import Tuberia
from interrogacion import BloqueInterrogacion
from BloqueIrrompible import BloqueIrrompible
from Poderes import Poderes
from moneda import Moneda
from Nubes import Nube
from Montanas import Montana
from meta import Meta
from Goomba import Goomba
from KoopaTroopa import Koopa_Troopa
import pyxel


class Draw():
    # Dibujar el Mario
    def DrawMario(self, mario: Mario):
        if not isinstance(mario, object):
            raise TypeError("mario debe ser un objeto ")
        pyxel.blt(mario.x,
                  mario.y,
                  0,
                  mario.spx,
                  mario.spy,
                  mario.w,
                  mario.h,
                  12)

    # Dibujar el suelo
    def DrawBloquesSuelo(self, bloques: Bloque):
        if not isinstance(bloques, object):
            raise TypeError("bloques debe ser un objeto ")
        pyxel.blt(bloques.x, bloques.y, 0, 0, 227, bloques.w, bloques.h, 12)

    # Dibujar las tuberías
    def DrawTuberias(self, tuberia: Tuberia):
        if not isinstance(tuberia, object):
            raise TypeError("tuberia debe ser un objeto ")
        pyxel.blt(tuberia.x, tuberia.y, 0, 79, 178, tuberia.w, tuberia.h, 12)

    # Dibujar los bloques irrompibles
    def DrawBloquesIrrompibles(self, bloqueIrrompible: BloqueIrrompible):
        if not isinstance(bloqueIrrompible, object):
            raise TypeError("BloqueIrrompible debe ser un objeto ")
        pyxel.blt(bloqueIrrompible.x, bloqueIrrompible.y, 0, 0, 62, bloqueIrrompible.w, bloqueIrrompible.h, 12)

    # Dibujar los bloques de interrogación
    def DrawBloqueInterrogacion(self, interrogacion: BloqueInterrogacion):
        if not isinstance(interrogacion, object):
            raise TypeError("Interrogación debe ser un objeto ")
        if interrogacion.activo:
            pyxel.blt(interrogacion.x, interrogacion.y, 0, 177, 27, interrogacion.w, interrogacion.h, 12)
        elif not interrogacion.activo:
            pyxel.blt(interrogacion.x, interrogacion.y, 0, 145, 27, interrogacion.w, interrogacion.h, 12)

    # Dibujar los bloques rompibles
    def DrawBLoqueRompible(self, bloqueRompible: Bloque):
        if not isinstance(bloqueRompible, object):
            raise TypeError("Bloques debe ser un objeto ")
        pyxel.blt(bloqueRompible.x, bloqueRompible.y, 0, 160, 200, bloqueRompible.w, bloqueRompible.h, 12)

    # Dibujar los poderes
    def DrawPoderes(self, poderes: Poderes):
        if not isinstance(poderes, object):
            raise TypeError("Bloques debe ser un objeto ")
        if poderes.is_activo:
            pyxel.blt(poderes.x, poderes.y, 0, poderes.sprite_x, poderes.sprite_y, poderes.w, poderes.h, 12)

    # Dibujar la puntiación
    def DrawScore(self, score):
        if not isinstance(score, str):
            raise TypeError("Score debe ser una cadena de texto")
        pyxel.text(4, 4, score, 7)

    # Dibujar la puntuación de monedas
    def DrawMonedas(self, monedas):
        if not isinstance(monedas, str):
            raise TypeError("Monedas debe ser una cadena de texto ")
        pyxel.blt(50, 2, 0, 81, 16, 5, 8, 12)
        pyxel.text(56, 4, monedas, 7)

    # Dibujar el texto del mundo
    def DrawMundo(self):
        pyxel.text(100, 4, "WORLD\n 1-1", 7)

    # Dibujar las vidas
    def DrawVidas(self, vidas):
        if not isinstance(vidas, str):
            raise TypeError("Bloques debe ser un objeto ")
        pyxel.text(180, 130, vidas, 7)

    # Dibujar al mario pequeño de las de las vidas
    def DrawMiniMario(self):
        pyxel.blt(167, 125, 0, 36, 84, 9, 13, 12)

    # Dibujar el tiempo
    def DrawTime(self, time):
        pyxel.text(150, 4, time, 7)

    # Dibujar las monedas
    def DrawMoneda(self, moneda: Moneda):
        if not isinstance(moneda, object):
            raise TypeError("Moneda debe ser un objeto ")
        pyxel.blt(moneda.x, moneda.y, 0, 2, 29, moneda.w, moneda.h, 12)

    # Dibujar las nubes
    def DrawNube(self, nube: Nube):
        if not isinstance(nube, object):
            raise TypeError("Nube debe ser un objeto ")
        pyxel.blt(nube.x, nube.y, 0, 108, 139, 46, 21, 12)

    # Dibujar las montañas
    def DrawMontana(self, montana: Montana):
        if not isinstance(montana, object):
            raise TypeError("Montana debe ser un objeto ")
        pyxel.blt(montana.x, montana.y, 0, 0, 181, 75, 45, 12)

    # Dibujar la meta
    def DrawMeta(self, meta: Meta):
        if not isinstance(meta, object):
            raise TypeError("Meta debe ser un objeto ")
        pyxel.blt(meta.x, meta.y, 0, 233, 121, meta.w, meta.h, 12)
        pyxel.blt(meta.x + 16, meta.y + 14, 0, 155, 134, 74, 92, 12)

    # Dibujar el goomba
    def DrawGoomba(self, goomba: Goomba):
        if not isinstance(goomba, object):
            raise TypeError("Goomba debe ser un objeto ")
        pyxel.blt(goomba.x, goomba.y, 1, 0, 0, goomba.w, goomba.h, 12)

    # Dibujar el goomba cuando muere
    def DrawGoombaMuerto(self, goomba: Goomba):
        if not isinstance(goomba, object):
            raise TypeError("Goomba debe ser un objeto ")
        pyxel.blt(goomba.x, goomba.y + 7, 1, 0, 23, goomba.w, goomba.h, 12)

    # Dibujar el Koopa Troopa
    def DrawKoopa(self, koopa: Koopa_Troopa):
        if not isinstance(koopa, object):
            raise TypeError("Koopa debe ser un objeto ")
        pyxel.blt(koopa.x, koopa.y, 1, 0, 40, koopa.w, koopa.h, 12)

    # Dibujar el Koopa en forma de caparazón
    def DrawCaparazon(self, koopa: Koopa_Troopa):
        if not isinstance(koopa, object):
            raise TypeError("Koopa debe ser un objeto ")
        pyxel.blt(koopa.x, koopa.y + 8, 1, 0, 64, 15, 15, 12)

    # Dibujar la pantalla de perder
    def DrawGameOver(self):
        pyxel.cls(0)
        pyxel.text(77, 63, "GAME OVER" , 8)
        pyxel.text(74, 63, "\n \n Pulsa q \n para cerrar ", 7)

    # Dibujar la pantalla del ganar
    def DrawFinal(self, mario: Mario):
        if not isinstance(mario, object):
            raise TypeError("Mario debe ser un objeto ")
        pyxel.cls(10)
        pyxel.text(77, 63, "YOU WIN" , 8)
        pyxel.text(74, 63, "\n \n Pulsa q \n para cerrar ", 7)
        pyxel.text(70, 100, "TU PUNTUACIÓN: {}".format(mario.score), 8)
