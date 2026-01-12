import pygame

def manejar_eventos_leer(evento, estado):
    if evento.type == pygame.QUIT:
        estado.ejecutando = False

    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        x, y = evento.pos

        # -------------------------------------------------
        # BOTONES DEL MODO LEER (y = 560–640)
        # -------------------------------------------------
        if 560 <= y <= 640:

            # COLOR (invertir tablero)
            if 528 <= x < 528 + 70:
                estado.tablero = estado.tablero.mirror()

            # DESHACER
            elif 528 + 80 <= x < 528 + 150:
                if estado.indice >= 0:
                    estado.tablero.pop()
                    estado.indice -= 1
                    estado.jugadas.pop()

            # SALIR
            elif 528 + 160 <= x < 528 + 230:
                estado.ejecutando = False
