import chess
from nucleo.movimiento import mover_pieza

def detectar_coronacion(tablero, movimiento):
    return tablero.piece_at(movimiento.from_square).piece_type == chess.PAWN and (
        chess.square_rank(movimiento.to_square) == 0 or chess.square_rank(movimiento.to_square) == 7
    )

def pedir_coronacion(estado, origen, destino):
    estado.coronando = True
    estado.coronacion_origen = origen
    estado.coronacion_destino = destino
    estado.opciones_coronacion = ["q", "r", "b", "n"]
    estado.opcion_seleccionada = None

def aplicar_coronacion(estado, pieza):
    movimiento = chess.Move(
        from_square=estado.coronacion_origen,
        to_square=estado.coronacion_destino,
        promotion=chess.Piece.from_symbol(pieza).piece_type
    )
    mover_pieza(estado, movimiento)
    estado.coronando = False
    estado.coronacion_origen = None
    estado.coronacion_destino = None
    estado.opciones_coronacion = []
    estado.opcion_seleccionada = None
