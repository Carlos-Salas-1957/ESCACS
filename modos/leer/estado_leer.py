import chess

class EstadoLeer:
    def __init__(self):
        # Tablero principal
        self.tablero = chess.Board()

        # Lista de jugadas en SAN
        self.movimientos = []

        # Casilla seleccionada por el usuario (None si no hay selección)
        self.seleccion = None

        # Turno actual (True = blancas, False = negras)
        self.turno_blancas = True

        # Scroll del panel de jugadas
        self.scroll = 0

        # Estado de coronación
        self.coronando = False
        self.coronacion_origen = None
        self.coronacion_destino = None
        self.opciones_coronacion = []
        self.opcion_seleccionada = None

        # Control del bucle principal del modo LEER
        self.ejecutando = True
