class EstadoLeer:
    def __init__(self):
        self.posicion = {
            # Blancas
            "a1": "wr", "b1": "wn", "c1": "wb", "d1": "wq", "e1": "wk", "f1": "wb", "g1": "wn", "h1": "wr",
            "a2": "wp", "b2": "wp", "c2": "wp", "d2": "wp", "e2": "wp", "f2": "wp", "g2": "wp", "h2": "wp",
            # Negras
            "a8": "br", "b8": "bn", "c8": "bb", "d8": "bq", "e8": "bk", "f8": "bb", "g8": "bn", "h8": "br",
            "a7": "bp", "b7": "bp", "c7": "bp", "d7": "bp", "e7": "bp", "f7": "bp", "g7": "bp", "h7": "bp"
        }

        self.jugadas = []
        self.historial = []
        self.turno = "blancas"
        self.seleccion = None
        self.ultima_jugada = None
        self.orientacion = "normal"
        self.ejecutando = True
        self.tablero_chess = None
