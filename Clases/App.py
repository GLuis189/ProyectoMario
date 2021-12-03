import pyxel

import Mario
import Nivel as Nv


class App():
    def __init__(self):
        pyxel.init(192, 128, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60)
        pyxel.load("assets/mario_assets.pyxres")
        pyxel.run(self.update, self.draw)
        self.__nivel = Nv


#Luego crearemos update y draw
    def update(self):
        pass

    def draw(self):
        pyxel.cls(6)
        Nv.draw


App()