import Bloques
import pyxel

import Mario
class Nivel():
    def __init__(self):
        self.__suelo = self.__crearSuelo()
        self.enemigos = None
        self.Mario = None
        self.Montanas = self.__crearMontanas
        self.mario = Mario()

    def __crearSuelo(self):
        items = []
        for i in range(10):
            items.append((i, i + 10))

        return items

    def draw(self):
        #dibujar suelo
        for item in self.__suelo:
            Bloques.Bloque_Suelo()
        #dibujar jugador


    def __crearMontanas(self): #En pycharm me sale subrayado al poner Montañas por la ñ asi que he puesto Montana
        pass

