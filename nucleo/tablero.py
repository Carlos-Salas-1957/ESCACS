import pygame
from nucleo.constantes import TAM_CASILLA, COLOR_CLARO, COLOR_OSCURO
from nucleo.cargador_piezas import cargar_imagen_pieza


def dibujar_tablero(pantalla):
    for fila in range(8):
        for col in range(8):
            color = COLOR_CLARO if (fila + col) % 2 == 0 else COLOR_OSCURO
            x = col * TAM_CASILLA
            y = fila * TAM_CASILLA
            pygame.draw.rect(pantalla, color, (x, y, TAM_CASILLA, TAM_CASILLA))


def dibujar_piezas(pantalla, tablero):
    """
    Dibuja las piezas según el estado del tablero de python-chess.
    """
    for fila in range(8):
        for col in range(8):
            square = (7 - fila) * 8 + col  # conversión fila/col → índice python-chess
            pieza = tablero.piece_at(square)

            if pieza:
                imagen = cargar_imagen_pieza(pieza.symbol())
                x = col * TAM_CASILLA
                y = fila * TAM_CASILLA
                pantalla.blit(imagen, (x, y))
