import chess

class EstadoReproducir:
    def __init__(self, tablero_inicial, movimientos):
        self.tablero = tablero_inicial
        self.movimientos = movimientos      # lista de movimientos python-chess
        self.indice = -1                    # -1 = posición inicial
        self.ejecutando = True
