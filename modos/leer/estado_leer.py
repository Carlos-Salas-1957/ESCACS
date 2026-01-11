from nucleo.posiciones import POSICION_INICIAL

class EstadoLeer:
    def __init__(self):
        self.posicion = POSICION_INICIAL.copy()
        self.historial = []          # lista de diccionarios de posición
        self.seleccion = None
        self.orientacion = "normal"
        self.jugadas = []            # [num, blanca, negra] con texto
        self.turno = "blancas"
        self.ultima_jugada = None
