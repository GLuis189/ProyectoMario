import pyxel


class Bloque(object):
    def __init__(self, posicion_x: int, posicion_y: int):
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y



class Bloque_Rompibles(Bloque):
    def __init__(self, posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Rompible = True


class Bloque_Suelo(Bloque):
    def __init__(self, posicion_x = 0, posicion_y = 20):
        super().__init__(posicion_x, posicion_y)

    def draw(self):
        pyxel.blt(self.Posicion_X, self.Posicion_Y, 0, 0, 62, 15, 15)


class Bloque_Irompibles(Bloque):
    def __init__(self, posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Rompible = False
    def draw(self):
        pass


class BLoque_Interrogacion(Bloque):
    def __init__(self, posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Activado = False
        self.Contenido = [0, [0, 1, 2]]
    def draw(self):
        pass

