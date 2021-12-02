import pyxel
from Clases import Bloques
import Mario
class App():
    def __init__(self):
        pyxel.init(192, 128, caption="Mario Bross", quit_key=pyxel.KEY_Q, fps=60)
        #pyxel.load("mario_assets.pyxres")
        pyxel.run(self.update, self.draw)
        self.Bloque_Rompible = Bloque_Rompibles(20, 20)


#Luego crearemos update y draw
    def update(self):
        pass

    def draw(self):
        pyxel.cls(6)
        self.Bloque_Rompible(Bloques).draw()

App()