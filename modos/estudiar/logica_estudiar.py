import pygame

def manejar_eventos_estudiar(evento, estado):
    if evento.type == pygame.QUIT:
        estado.ejecutando = False

    if evento.type == pygame.MOUSEBUTTONDOWN:
        x, y = evento.pos

        # Botón SALIR
        if 800 <= x <= 880 and 448 <= y <= 512:
            estado.ejecutando = False

        # Botón COLOR (lo implementaremos cuando toque)
        # Botón CARGAR (lo implementaremos cuando toque)
        # Botón INFO (lo implementaremos cuando toque)

        # Aquí irá la lógica de clic en el tablero para estudiar posiciones
