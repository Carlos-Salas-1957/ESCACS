import pygame
from nucleo.constantes import ANCHO_TABLERO, ALTO_TABLERO


def dibujar_botones_leer(pantalla, estado):
    fuente = pygame.font.SysFont(None, 22)

    x_base = ANCHO_TABLERO + 30
    y_base = ALTO_TABLERO - 55

    # texto visible, nombre lógico, rectángulo
    botones = [
        ("Color", "color",     pygame.Rect(x_base,          y_base, 70, 35)),
        ("Undo",  "deshacer",  pygame.Rect(x_base + 80,     y_base, 70, 35)),
        ("Salir", "salir",     pygame.Rect(x_base + 160,    y_base, 70, 35)),
    ]

    mouse = pygame.mouse.get_pos()

    for texto, nombre, rect in botones:
        color_fondo = (100, 100, 100) if rect.collidepoint(mouse) else (70, 70, 70)

        pygame.draw.rect(pantalla, color_fondo, rect, border_radius=6)
        pygame.draw.rect(pantalla, (220, 220, 220), rect, 2, border_radius=6)

        render = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(
            render,
            (
                rect.x + (rect.width - render.get_width()) // 2,
                rect.y + (rect.height - render.get_height()) // 2,
            ),
        )


def detectar_click_boton(x, y):
    x_base = ANCHO_TABLERO + 30
    y_base = ALTO_TABLERO - 55

    botones = {
        "color":    pygame.Rect(x_base,          y_base, 70, 35),
        "deshacer": pygame.Rect(x_base + 80,     y_base, 70, 35),
        "salir":    pygame.Rect(x_base + 160,    y_base, 70, 35),
    }

    for nombre, rect in botones.items():
        if rect.collidepoint(x, y):
            return nombre

    return None
