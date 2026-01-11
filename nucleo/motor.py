import chess

def crear_board():
    return chess.Board()

def board_a_posicion(board):
    pos = {}
    mapa = {
        "P": "P", "p": "p",
        "N": "C", "n": "c",
        "B": "A", "b": "a",
        "R": "T", "r": "t",
        "Q": "D", "q": "d",
        "K": "R", "k": "r",
    }
    for sq, piece in board.piece_map().items():
        file = chess.square_file(sq)
        rank = chess.square_rank(sq)
        casilla = chr(ord("a") + file) + str(rank + 1)
        pos[casilla] = mapa[piece.symbol()]
    return pos

# Ejecuta movimiento simple origen-destino (sin promoción explícita todavía)
# Devuelve (exito, san)
def ejecutar_simple(board, origen, destino):
    uci = origen + destino
    move = chess.Move.from_uci(uci)
    if move not in board.legal_moves:
        return False, None
    board.push(move)
    san = board.san(move)
    return True, san

def en_jaque(board):
    return board.is_check()
