import chess

class EstadoLeer:
    def __init__(self, tablero_inicial):
        self.tablero = tablero_inicial

        # Lista de movimientos python-chess (como REPRODUCIR)
        self.jugadas = []        

        # Índice de jugada actual
        self.indice = -1          # -1 = posición inicial

        # Información de la partida (para el botón INFO)
        self.evento = ""
        self.blancas = ""
        self.negras = ""
        self.fecha = ""
        self.resultado = ""

        self.ejecutando = True
