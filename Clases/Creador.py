
from Bloques import Bloque
from BloqueRompible import BloqueRompible
from tuberia import Tuberia
from interrogacion import BloqueInterrogacion
from BloqueIrrompible import BloqueIrrompible
from moneda import Moneda
from Nubes import Nube
from Montanas import Montana
from bloquemoneda import BloqueRompibleMoneda
from Goomba import Goomba
from KoopaTroopa import Koopa_Troopa


# Esta clase de Creador se engarga de crear todos los bloques, los objetos y los enemigos del mapa en distintas listas
class Creador():

    def crear_suelo(self, num_suelo):  # Se crea una lista llena de los bloques q conforman el suelo
        if not isinstance(num_suelo, int):
            raise TypeError("num_suelo debe ser un objeto de tipo entero")
        bloques = []
        cont = 0
        for i in range(num_suelo):
            cont += 1
            if cont < 16 or cont > 19 and cont < 46 or cont > 50:
                bloques.append(Bloque(16 * i, 144 - 16))  # Introduce en la lista un objeto tipo Bloque en esa posicion
        return bloques

    def crearBloquesIrrompibles(self):  # Se crea una lista llena de los bloques q conforman los bloques irrompibles
        #Crea los Bloques irrompibles
        bloques = [BloqueIrrompible(192, 112), BloqueIrrompible(208, 112), BloqueIrrompible(224, 112), BloqueIrrompible(208, 96), BloqueIrrompible(224, 96), BloqueIrrompible(224, 80), BloqueIrrompible(304, 112), BloqueIrrompible(704, 112), BloqueIrrompible(688, 112), BloqueIrrompible(704, 96), BloqueIrrompible(736, 60), BloqueIrrompible(720, 60)]
        return bloques

    def crearTuberias(self):  # Se crea una lista llena de los bloques q conforman las tuberias
        # Crea las tuberías del nivel
        bloques = [Tuberia(432, 112), Tuberia(544, 82)]
        return bloques

    def crearBloquesRompibles(self):  # Se crea una lista llena de los bloques q conforman los bloques irrompibles
        # Crea los bloques rimpibles del nivel
        bloques = [BloqueRompible(128, 64), BloqueRompible(352, 80), BloqueRompible(368, 80), BloqueRompible(384, 80), BloqueRompible(352, 26), BloqueRompible(624, 80), BloqueRompible(640, 80)]
        return bloques

    def crearInterrogacion(self):  # Se crea una lista llena de los bloques q conforman los bloques con interrogacion
        # Crea los bloques de interrogación prefedinidos
        bloques = [BloqueInterrogacion(166, 64), BloqueInterrogacion(368, 26)]
        return bloques

    def crearMonedas(self):  # Se crea una lista llena de las  monedas del mapa
        # Crea las monedas predefinidas
        monedas = [Moneda(148, 64), Moneda(368, 10), Moneda(352, 10), Moneda(384, 60), Moneda(736, 44), Moneda(669, 108)]
        return monedas

    def crearBloquesconmoneda(self):  # Se crea una lista llena de los bloques q conforman los bloques con monedas
        # Crea los bloques con monedas dentro
        bloques = [BloqueRompibleMoneda(640, 80)]
        return bloques

    def crearNubes(self):  # Se crea una lista llena de las nubes del fondo
        # Crea las nubes
        nubes = [Nube(10, 32), Nube(180, 16), Nube(290, 32), Nube(420, 26), Nube(560, 16), Nube(710, 16)]
        return nubes

    def crearMontanas(self):  # Se crea una lista llena de las montanas del fondo
        # crea las montanas
        montana = [Montana(0, 83), Montana(440, 83), Montana(628, 83)]
        return montana

    def crearGoombas(self):  # Se crea una lista llena de los Goombas del mapa
        # Crea una lista con los Goombas del mapa
        goombas = [Goomba(182, 112), Goomba(416, 112)]
        return goombas

    def crearEnemigos(self):
        enemigos = []
        return enemigos

    def crearKoopaTropa(self):  # Se crea una lista llena de los KoopaTroopa del mapa
        # Crea una lista con los KoopaTroopa del mapa
        koopatropa = [Koopa_Troopa(286, 105)]
        return koopatropa

