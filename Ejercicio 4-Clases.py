import pyxel

class App():
    def __init__(self):
        pyxel.init(256, 160, caption="Mario Bross")
        pyxel.load("mario_assets.pyxres")
        pyxel.run(self.update, self.draw)

#Luego crearemos update y draw
    def update(self):
       pass
    def draw(self):
        pass

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

class Enemigos(object):
    def __init__(self, posicion_x, posicion_y, velocidad_x, vivo):
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y
        self.Velocidad_X = velocidad_x
        self.Vivo = vivo

class Goomba(Enemigos):
    def __init__(self, posicion_x, posicion_y, velocidad_x):
        super().__init__(posicion_x, posicion_y, velocidad_x)
        self.Velocidad_X = self.mover()

    def mover(self):
        self.Velocidad_X = -2
        return velocidad_X

class Koopa_Troopa(Enemigos):
    def __init__(self, posicion_x, posicion_y, velocidad_x, concha):
        super().__init__(posicion_x, posicion_y, velocidad_x)
        self.Concha = concha

class Mario():
    def __init__(self, posicion_x: int, posicion_y: int, velocidad_x, velocidad_y, vidas, morir) -> None:
        self.Posicion_X = posicion_x
        self.Posicion_Y = posicion_y
        self.Velocidad_X = velocidad_x
        self.Velocidad_Y = velocidad_y
        self.Vidas = vidas
        self.Morir = morir

    def mover(self):
        self.Posicion_X += self.Velocidad_X
        self.Posicion_Y -= self.Velocidad_Y

    def Update(self):
        pass

    def Draw(self):
        pass

class Nivel():
    def __init__(self):
        self.bloques = self.__crearBloques()
        self.enemigos = None
        self.Mario = None
        self.Montanas = self.__crearMontanas

    def __crearBloques(self):
        return []

    def __crearMontanas(self): #En pycharm me sale subrayado al poner Montañas por la ñ asi que he puesto Montana
        return []

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
