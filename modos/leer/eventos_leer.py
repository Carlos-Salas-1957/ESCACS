import pygame
from nucleo.constantes import TAM_CASILLA
from modos.leer.botones_leer import detectar_click_boton
from modos.leer.logica_leer import procesar_click_leer

def manejar_eventos_leer(estado):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return "salir"

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos

            # Clic en el tablero
            if x < TAM_CASILLA * 8 and y < TAM_CASILLA * 8:
                fila = y // TAM_CASILLA
                col = x // TAM_CASILLA
                procesar_click_leer(estado, fila, col)

            # Clic en botones
            accion = detectar_click_boton(x, y)
            if accion == "color":
                estado.turno_blancas = not estado.turno_blancas
            elif accion == "deshacer":
                if len(estado.movimientos) > 0:
                    estado.tablero.pop()
                    estado.movimientos.pop()
            elif accion == "salir":
                return "salir"

    return None


