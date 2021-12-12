
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


class Creador():

    def crear_suelo(self, num_suelo):  # Se crea una lista llenas de los bloques q conforman el suelo
        bloques = []
        cont = 0
        for i in range(num_suelo):
            cont += 1
            if cont < 16 or cont > 19:
                bloques.append(Bloque(16 * i, 144 - 16))  # Con 16 * i, 128 - 16 consigues que se creen los bloques uno al lado del otro
        return bloques
    def crearBloquesIrrompibles(self):
        #Crea los Bloques irrompibles
        bloques = [BloqueIrrompible(192, 112), BloqueIrrompible(208, 112), BloqueIrrompible(224, 112), BloqueIrrompible(208, 96), BloqueIrrompible(224, 96), BloqueIrrompible(224, 80), BloqueIrrompible(304, 112), BloqueIrrompible(704, 112), BloqueIrrompible(704, 96), BloqueIrrompible(704, 80), BloqueIrrompible(688, 64), BloqueIrrompible(704, 64)]
        return bloques
    def crearTuberias(self):
        # Crea las tuberías del nivel
        bloques = [Tuberia(432, 112), Tuberia(544, 82)]
        return bloques
    def crearBloquesRompibles(self):
        # Crea los bloques rimpibles del nivel
        bloques = [BloqueRompible(128, 64), BloqueRompible(352, 80), BloqueRompible(368, 80), BloqueRompible(384, 80), BloqueRompible(352, 26), BloqueRompible(624, 80), BloqueRompible(640, 80)]
        return bloques
    def crearInterrogacion(self):
        # Crea los bloques de interrogación prefedinidos
        bloques = [BloqueInterrogacion(166, 64), BloqueInterrogacion(368, 26)]
        return bloques
    def crearMonedas(self):
        # Crea las monedas predefinidas
        monedas = [Moneda(148, 64), Moneda(368, 10), Moneda(352, 10), Moneda(384, 60), Moneda(704, 44), Moneda(685, 108)]
        return monedas
    def crearBloquesconmoneda(self):
        # Crea lso bloques con monedas dentro
        bloques = [BloqueRompibleMoneda(640, 80)]
        return bloques
    def crearEnemigos(self):
        enemigos = []
        return enemigos
    def crearNubes(self):
        nubes = [Nube(10, 32), Nube(180, 16), Nube(290, 32), Nube(420, 26), Nube(560, 16), Nube(710, 16)]
        return nubes
    def crearMontanas(self):
        montana = [Montana(0, 83), Montana(440, 83), Montana(628, 83)]
        return montana
    def crearGoombas(self):
        goombas = [Goomba(182, 112), Goomba(416, 112)]
        return goombas
    def crearKoopaTropa(self):
        koopatropa = [Koopa_Troopa(286, 105)]
        return koopatropa
