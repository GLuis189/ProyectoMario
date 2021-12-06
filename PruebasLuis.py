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

class App():
    def __init__(self):
        pyxel.init(192, 128, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60)
        pyxel.load("mario_assets.pyxres")

        self.Mario = Mario()

        self.Suelo = self.__crear_suelo(12)  # Con esta función creas el suelo
        self.Incognita = Incognita(20, 20)
        self.Ladrillos_Rompibles = Ladrillo_Rompible(40, 84)
        self.Ladrillos_Irrompibles = Ladrillo_Irrompible(60, 20)

        self.goomba = Goomba(128, 96)
        self.koopa = Koopa_Troopa(30, 30)

        self.Monedas = self.__crear_monedas(3)

        self.Poderes = Poder(70, 90)

        pyxel.playm(0, loop=True)
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
            monedas.append(Moneda(40 * i + 5, 80))
        return monedas

    # Luego crearemos update y draw
    def update(self):
        self.Mario.update()

        if (
                self.Mario.x + 10 >= self.Ladrillos_Rompibles.x
                and self.Mario.x <= self.Ladrillos_Rompibles.x + 11
                and self.Mario.y + 16 >= self.Ladrillos_Rompibles.y
                and self.Mario.y <= self.Ladrillos_Rompibles.y + 8

            ):
            self.Mario.colisionar(self.Ladrillos_Rompibles.y)

        # Asi es como he hecho que el suelo sea colisionable
        # Para un futuro podemos hacer una lista de los objetos colisionables y
        # con este algoritmo hacer que sea colisionable por arriba almenos
        for item in self.Suelo:
            #item.update(self.Mario)
            if (
                    self.Mario.x + 10 >= item.x
                    and self.Mario.x <= item.x + 11
                    and self.Mario.y + 16 >= item.y
                    and self.Mario.y <= item.y + 8

            ):
                self.Mario.colisionar(item.y)

        self.Poderes.update(self.Mario)

        self.goomba.update()  #Hay que hacer los setter para poder modificar la posicion del goomba

        #Con esto intento que si no está activa la moneda que se borre de la lista
        for item in self.Monedas:
            item.update(self.Mario)

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

        pyxel.blt(self.Ladrillos_Rompibles.x, self.Ladrillos_Rompibles.y, 0, self.Ladrillos_Rompibles.sprite_x,
                  self.Ladrillos_Rompibles.sprite_y, self.Ladrillos_Rompibles.w, self.Ladrillos_Rompibles.h, 12)
        pyxel.blt(self.Ladrillos_Irrompibles.x, self.Ladrillos_Irrompibles.y, 0, self.Ladrillos_Irrompibles.sprite_x,
                  self.Ladrillos_Irrompibles.sprite_y, self.Ladrillos_Irrompibles.w, self.Ladrillos_Irrompibles.h, 12)

        pyxel.blt(self.Poderes.x, self.Poderes.y, 0, self.Poderes.sprite_x, self.Poderes.sprite_y, self.Poderes.w, self.Poderes.h, 12)
App()
