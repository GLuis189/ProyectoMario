from Fondo import Fondo


class Nube(Fondo):
    def __init__(self, x, y):
        super().__init__(x, y)
        if not isinstance(x, int):
            raise TypeError("x debe ser un objeto de tipo entero")
        if not isinstance(y, int):
            raise TypeError("y debe ser un objeto de tipo entero")