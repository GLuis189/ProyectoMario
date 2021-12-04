import pyxel

from Clases1.bloque import Bloque
from Clases1.mario import Mario
# Hay que ver como va lo de las herencias
# class Suelo(Bloque):
#   pass

class Enemigos():
    pass


class Poderes():
    pass


class App():
    def __init__(self):
        pyxel.init(192, 128, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60)
        pyxel.load("mario_assets.pyxres")
        self.Suelo = self.__crear_suelo(12)  # Con esta función creas el suelo
        self.Mario = Mario()

        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    # Se crea una lista llenas de los bloques q conforman el suelo
    def __crear_suelo(self, num_suelo):
        bloques = []
        for i in range(num_suelo):
            bloques.append(Bloque(16 * i,
                                  128 - 16))  # Con 16 * i, 128 - 16 consigues que se creen los bloques uno al lado del otro
        return bloques

    # Luego crearemos update y draw
    def update(self):
        self.Mario.update()

        for item in self.Suelo:
            item.update(self.Mario)

    def draw(self):
        pyxel.cls(6)

        self.Mario.draw()

        # Hay que dibujar los bloques y así se dibujan ya q estan dentro de una lista
        for item in self.Suelo:
            pyxel.blt(item.x, item.y, 0, 0, 227, item.w, item.h, 12)


App()
