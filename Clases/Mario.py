

class Mario():
    def __init__(self, posicion_x: int, posicion_y: int) -> None:
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y
        self. velocidad = 0
    def mover(self):
        #Presionar Q para q se mueva si no esta mas de la mitad de la pantalla.
