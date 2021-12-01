

class Bloques(object):
    def __init__(self, posicion_x: int, posicion_y: int) -> None:
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y
        self.Rompible = None


class Bloques_Rompibles(Bloques):
    def __init__(self, posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Rompible = True


class Bloques_Irompibles(Bloques):
    def __init__(self, posicion_x: int, posicion_y: int):
        super().__init__(posicion_x, posicion_y)
        self.Rompible = False
