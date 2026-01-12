import pygame

def manejar_eventos_menu(evento, estado):
    if evento.type == pygame.QUIT:
        estado.ejecutando = False
        return "salir"

    if evento.type == pygame.MOUSEBUTTONDOWN:
        x, y = evento.pos

        # LEER
        if 200 <= x <= 440 and 180 <= y <= 230:
            estado.ejecutando = False
            return "leer"

        # REPRODUCIR
        if 200 <= x <= 440 and 250 <= y <= 300:
            estado.ejecutando = False
            return "reproducir"

        # ESTUDIAR
        if 200 <= x <= 440 and 320 <= y <= 370:
            estado.ejecutando = False
            return "estudiar"

        # SALIR
        if 200 <= x <= 440 and 390 <= y <= 440:
            estado.ejecutando = False
            return "salir"

    return None
