import pygame
import chess
from nucleo.coronacion import detectar_coronacion
from nucleo.movimiento import mover_pieza

def procesar_click_leer(estado, fila, col):
    if estado.coronando:
        # Esperando selección de pieza
        for i, rect in enumerate(estado.rects_coronacion):
            if rect.collidepoint(col * 60, fila * 60):
                tipo = [chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT][i]
                movimiento = chess.Move(estado.origen_coronacion, estado.destino_coronacion, promotion=tipo)
                mover_pieza(estado, movimiento)
                estado.coronando = False
                estado.rects_coronacion = []
                estado.origen_coronacion = None
                estado.destino_coronacion = None
                estado.seleccion = None
        return

    fila_real = 7 - fila
    casilla = chess.square(col, fila_real)

    if estado.seleccion is None:
        pieza = estado.tablero.piece_at(casilla)
        if pieza and pieza.color == estado.tablero.turn:
            estado.seleccion = casilla
    else:
        origen = estado.seleccion
        destino = casilla
        movimiento = chess.Move(from_square=origen, to_square=destino)

        if detectar_coronacion(estado.tablero, movimiento):
            estado.coronando = True
            estado.origen_coronacion = origen
            estado.destino_coronacion = destino
            estado.rects_coronacion = generar_rects_coronacion()
        elif movimiento in estado.tablero.legal_moves:
            mover_pieza(estado, movimiento)

        estado.seleccion = None


def generar_rects_coronacion():
    # Cuatro rectángulos horizontales en el centro del tablero
    base_x = 60 * 2
    base_y = 60 * 3
    ancho = 60
    alto = 60
    return [pygame.Rect(base_x + i * ancho, base_y, ancho, alto) for i in range(4)]
