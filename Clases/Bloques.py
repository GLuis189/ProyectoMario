

class Bloque(object):
    def __init__(self, posicion_x: int, posicion_y: int) -> None:
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y

class Bloque_Rompibles(Bloque):
    def __init__(self, posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Rompible = True

class Bloque_Irompibles(Bloque):
    def __init__(self, posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Rompible = False

class BLoque_Interrogacion(Bloque):
    def __init__(self, posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Activado = False
        self.Contenido = [0,[0,1,2]]

