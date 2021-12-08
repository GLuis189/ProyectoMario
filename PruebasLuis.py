import pyxel

from Clases1.mario import Mario

from Clases1.bloque import Suelo
from Clases1.bloque import Incognita
from Clases1.bloque import Ladrillo_Rompible
from Clases1.bloque import Ladrillo_Irrompible

from Clases1.enemigos import Goomba
from Clases1.enemigos import Koopa_Troopa

from Clases1.moneda import Moneda

from Clases1.poderes import Poder

from Clases1.fondo import Nube
from Clases1.fondo import Montana


class App():
    def __init__(self):
        pyxel.init(192, 128, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60, scale=4)
        pyxel.load("mario_assets.pyxres")

        self.Mario = Mario()

        self.Suelo = self.__crear_suelo(12)  # Con esta función creas el suelo
        self.Incognita = Incognita(20, 20)
        self.Ladrillos_Rompibles = Ladrillo_Rompible(40, 40)
        self.Ladrillos_Irrompibles = Ladrillo_Irrompible(60, 20)

        self.goomba = Goomba(128, 96)
        self.koopa = Koopa_Troopa(100, 30)

        self.Monedas = self.__crear_monedas(3)

        self.Poderes = self.__crear_poderes(2)

        self.Nubes = Nube(70, 20)
        self.Montana

        pyxel.run(self.update, self.draw)


    # Se crea una lista llenas de los bloques q conforman el suelo
    def __crear_suelo(self, num_suelo):
        bloques = []
        for i in range(num_suelo):
            bloques.append(Suelo(16 * i, 112))  # Con 16 * i, 128 - 16 consigues que se creen los bloques uno al lado del otro
        return bloques

    def __crear_monedas(self, num_monedas):
        monedas = []
        for i in range(num_monedas):
            monedas.append(Moneda(40 * i, 80))
        return monedas

    def __crear_poderes(self, num_poderes):
        poderes = []
        for i in range(num_poderes):
            poderes.append(Poder(20 * i, 80))
        return poderes

    # Luego crearemos update y draw
    def update(self):
        self.Mario.update()
        for item in self.Poderes:
            item.update(self.Mario)
            if (self.Mario.x + abs(self.Mario.w) >= item.x and self.Mario.x <= item.x + item.w
                    and self.Mario.y + self.Mario.h >= item.y and self.Mario.y <= item.y + item.h):
                self.Mario.tocar_poder()


        if (
                self.Mario.x + abs(self.Mario.w) >= self.Ladrillos_Rompibles.x
                and self.Mario.x <= self.Ladrillos_Rompibles.x + self.Ladrillos_Rompibles.w
                and self.Mario.y + self.Mario.h >= self.Ladrillos_Rompibles.y
                and self.Mario.y <= self.Ladrillos_Rompibles.y + self.Ladrillos_Rompibles.h

            ):
            self.Mario.colisionar_arriba(self.Ladrillos_Rompibles.y)

        if (
                self.Ladrillos_Rompibles.x <= self.Mario.x <= self.Ladrillos_Rompibles.x + self.Ladrillos_Rompibles.w
                and self.Ladrillos_Rompibles.y <= self.Mario.y <= self.Ladrillos_Rompibles.y - self.Ladrillos_Rompibles.h):
            self.Mario.colisionar_abajo(self.Ladrillos_Rompibles.y)

        # Asi es como he hecho que el suelo sea colisionable
        # Para un futuro podemos hacer una lista de los objetos colisionables y
        # con este algoritmo hacer que sea colisionable por arriba almenos
        for item in self.Suelo:
            if (
                 self.Mario.x + abs(self.Mario.w) >= item.x
                    and self.Mario.x <= item.x + item.w
                    and self.Mario.y + self.Mario.h >= item.y
                    and self.Mario.y <= item.y + item.h

            ):
                self.Mario.colisionar_arriba(item.y)


        self.goomba.update()  #Hay que hacer los setter para poder modificar la posicion del goomba

        #Con esto intento que si no está activa la moneda que se borre de la lista
        for item in self.Monedas:
            item.update_moneda(self.Mario)

        self.Incognita.update(self.Mario)

    def draw(self):
        pyxel.cls(6)

        self.Mario.draw()

        # Hay que dibujar los bloques y así se dibujan ya q estan dentro de una lista
        for item in self.Suelo:
            pyxel.blt(item.x, item.y, 0, item.sprite_x, item.sprite_y, item.w, item.h, 12)



        pyxel.blt(self.goomba.x, self.goomba.y, 1, self.goomba.sprite_x, self.goomba.sprite_y, self.goomba.w, self.goomba.h, 12)
        pyxel.blt(self.koopa.x, self.koopa.y, 1, self.koopa.sprite_x, self.koopa.sprite_y, self.koopa.w, self.koopa.h, 12)

        for item in self.Monedas:
            if item.is_active:
                item.draw()

        for item in self.Poderes:
            if item.is_active:
                pyxel.blt(item.x, item.y, 0, item.sprite_x, item.sprite_y,
                          item.w, item.h, 12)

        pyxel.blt(self.Ladrillos_Rompibles.x, self.Ladrillos_Rompibles.y, 0, self.Ladrillos_Rompibles.sprite_x,
                  self.Ladrillos_Rompibles.sprite_y, self.Ladrillos_Rompibles.w, self.Ladrillos_Rompibles.h, 12)
        pyxel.blt(self.Ladrillos_Irrompibles.x, self.Ladrillos_Irrompibles.y, 0, self.Ladrillos_Irrompibles.sprite_x,
                  self.Ladrillos_Irrompibles.sprite_y, self.Ladrillos_Irrompibles.w, self.Ladrillos_Irrompibles.h, 12)
        pyxel.blt(self.Incognita.x, self.Incognita.y, 0, self.Incognita.sprite_x,
                  self.Incognita.sprite_y, self.Incognita.w, self.Incognita.h, 12)

        pyxel.blt(self.Nubes.x, self.Nubes.y, 0, 139, 46, 62, 16, 12)

App()
