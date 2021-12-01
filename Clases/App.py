import pyxel
import Mario
class App():
    def __init__(self):
        pyxel.init(256, 160, caption="Mario Bross")
        #pyxel.load("mario_assets.pyxres")
        pyxel.run(self.update, self.draw)

#Luego crearemos update y draw
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pass
App()