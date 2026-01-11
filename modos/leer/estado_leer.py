from nucleo.posiciones import POSICION_INICIAL

class EstadoLeer:
    def __init__(self):
        self.posicion = POSICION_INICIAL.copy()
        self.historial = []
        self.turno = "w"
        self.orientacion = "normal"
