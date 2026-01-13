import chess

def mover_pieza(estado, movimiento: chess.Move):
    # Obtener la SAN ANTES de hacer el push
    san = estado.tablero.san(movimiento)

    # Aplicar el movimiento al tablero
    estado.tablero.push(movimiento)

    # Guardar la jugada en la lista de movimientos del estado
    if not hasattr(estado, "movimientos"):
        estado.movimientos = []

    estado.movimientos.append(san)
