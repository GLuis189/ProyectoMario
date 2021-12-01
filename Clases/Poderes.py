class Poderes():
    def __init__(self, posicion_x,posicion_y, activo):
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y
        self.Activo = activo

class Seta(Poderes):
    def __init__(self, posicion_x, posicion_y, tipo):
        super().__init__(posicion_x, posicion_y, tipo)
        self.Tipo = tipo
    def Crecer(self):
        #Mario pequeño pasa a Super Mario

class Flor_Fuego(Poderes):
    def __init__(self, posicion_x, posicion_y, tipo):
        super().__init__(posicion_x, posicion_y, tipo)
        self.Tipo = tipo
    def (self):
        #Super Mario se conveirte en Mario de fuego y lanza bolas de fuego.

class Estrella(Poderes):
    def __init__(self, posicion_x, posicion_y, tipo):
        super().__init__(posicion_x, posicion_y, tipo)
        self.Tipo = tipo
    def Invencible(self):
        #Mario se vuelve invencible y mata lo que toca