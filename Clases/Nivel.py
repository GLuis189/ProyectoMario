import Bloques
import pyxel


class Nivel():
    def __init__(self):
        self.__suelo = self.__crearSuelo()
        self.enemigos = None
        self.Mario = None
        self.Montanas = self.__crearMontanas

    def __crearSuelo(self):
        items = []
        for i in range(10):
            for j in range(10):
                items.append((i, j + 20))

        return items

    def draw(self):
        for item in self.__suelo:
            Bloques.Bloque_Suelo(10, 10)

    def __crearMontanas(self): #En pycharm me sale subrayado al poner Montañas por la ñ asi que he puesto Montana
        pass

