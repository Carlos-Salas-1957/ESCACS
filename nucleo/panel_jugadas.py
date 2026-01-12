import pygame

def dibujar_panel_jugadas(pantalla, estado, x, y, ancho, alto):
    pygame.draw.rect(pantalla, (40, 40, 40), (x, y, ancho, alto))

    fuente = pygame.font.SysFont("arial", 20)

    # ---------------------------------------------------------
    # COMPATIBILIDAD ENTRE MODOS
    # REPRODUCIR → estado.movimientos
    # LEER / ESTUDIAR → estado.jugadas
    # ---------------------------------------------------------
    movimientos = getattr(estado, "movimientos", None)
    if movimientos is None:
        movimientos = getattr(estado, "jugadas", [])

    indice = getattr(estado, "indice", -1)

    # ---------------------------------------------------------
    # CONVERTIR MOVIMIENTOS EN PARES (blancas, negras)
    # ---------------------------------------------------------
    pares = []
    for i in range(0, len(movimientos), 2):
        blancas = movimientos[i]
        negras = movimientos[i + 1] if i + 1 < len(movimientos) else ""
        pares.append((str(blancas), str(negras)))

    # ---------------------------------------------------------
    # SCROLL AUTOMÁTICO
    # ---------------------------------------------------------
    total_filas = len(pares)
    filas_visibles = alto // 24
    inicio = max(0, total_filas - filas_visibles)

    # ---------------------------------------------------------
    # DIBUJAR FILAS
    # ---------------------------------------------------------
    for fila, (blancas, negras) in enumerate(pares[inicio:], start=inicio):
        y_fila = y + (fila - inicio) * 24

        # Resaltar jugada activa
        if fila * 2 <= indice < (fila + 1) * 2:
            pygame.draw.rect(pantalla, (70, 70, 70), (x, y_fila, ancho, 24))

        # Número de jugada
        num = str(fila + 1)
        pantalla.blit(fuente.render(num, True, (200, 200, 200)), (x + 8, y_fila + 2))

        # Jugada blancas
        pantalla.blit(fuente.render(blancas, True, (255, 255, 255)), (x + 40, y_fila + 2))

        # Jugada negras
        pantalla.blit(fuente.render(negras, True, (255, 255, 255)), (x + 160, y_fila + 2))
