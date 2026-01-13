import pygame

def dibujar_panel_jugadas(pantalla, estado, x, y, ancho, alto):
    pygame.draw.rect(pantalla, (40, 40, 40), (x, y, ancho, alto))

    fuente = pygame.font.SysFont("arial", 20)

    # Cabecera
    pantalla.blit(fuente.render("Num", True, (255, 255, 255)), (x + 8, y + 4))
    pantalla.blit(fuente.render("Blancas", True, (255, 255, 255)), (x + 40, y + 4))
    pantalla.blit(fuente.render("Negras", True, (255, 255, 255)), (x + 160, y + 4))

    pygame.draw.line(pantalla, (200, 200, 200), (x, y + 28), (x + ancho, y + 28), 1)

    y += 32  # margen para las jugadas

    # Compatibilidad entre modos
    movimientos = getattr(estado, "movimientos", None)
    if movimientos is None:
        movimientos = getattr(estado, "jugadas", [])

    indice = getattr(estado, "indice", -1)

    # Convertir movimientos en pares
    pares = []
    for i in range(0, len(movimientos), 2):
        blancas = movimientos[i]
        negras = movimientos[i + 1] if i + 1 < len(movimientos) else ""
        pares.append((str(blancas), str(negras)))

    # Scroll automático
    total_filas = len(pares)
    filas_visibles = (alto - 32) // 24
    inicio = max(0, total_filas - filas_visibles)

    # Dibujar filas
    for fila, (blancas, negras) in enumerate(pares[inicio:], start=inicio):
        y_fila = y + (fila - inicio) * 24

        # Resaltar jugada activa
        if fila * 2 <= indice < (fila + 1) * 2:
            pygame.draw.rect(pantalla, (70, 70, 70), (x, y_fila, ancho, 24))

        pantalla.blit(fuente.render(str(fila + 1), True, (200, 200, 200)), (x + 8, y_fila + 2))
        pantalla.blit(fuente.render(blancas, True, (255, 255, 255)), (x + 40, y_fila + 2))
        pantalla.blit(fuente.render(negras, True, (255, 255, 255)), (x + 160, y_fila + 2))
