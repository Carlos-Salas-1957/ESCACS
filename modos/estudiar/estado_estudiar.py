import chess

class EstadoEstudiar:
    def __init__(self, tablero_inicial=None):
        self.tablero = tablero_inicial if tablero_inicial else chess.Board()
        self.historial = []      # lista de movimientos (python-chess)
        self.ejecutando = True
