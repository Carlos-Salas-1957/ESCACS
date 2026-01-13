import pygame
from nucleo.constantes import (
    ANCHO_TABLERO,
    ALTO_TABLERO,
    ANCHO_PANEL,
    COLOR_FONDO_PANEL
)
from nucleo.tablero import dibujar_tablero, dibujar_piezas
from nucleo.panel_jugadas import dibujar_panel_jugadas
from modos.leer.botones_leer import dibujar_botones_leer


def dibujar_interfaz_leer(pantalla, estado):
    # Fondo general
    pantalla.fill((220, 220, 220))

    # 1. TABLERO
    dibujar_tablero(pantalla)
    dibujar_piezas(pantalla, estado.tablero)

    # 2. PANEL DE JUGADAS
    x_panel = ANCHO_TABLERO + 20
    y_panel = 40
    ancho_panel = ANCHO_PANEL - 40
    alto_panel = ALTO_TABLERO - 120

    pygame.draw.rect(pantalla, COLOR_FONDO_PANEL, (x_panel, y_panel, ancho_panel, alto_panel))

    dibujar_panel_jugadas(
        pantalla,
        estado,
        x_panel,
        y_panel,
        ancho_panel,
        alto_panel
    )

    # 3. BOTONES
    dibujar_botones_leer(pantalla, estado)

    # 4. MODAL DE CORONACIÓN (si está activo)
    if getattr(estado, "coronando", False):
        dibujar_modal_coronacion(pantalla, estado)

    pygame.display.flip()



# ---------------------------------------------------------
# DIBUJAR MODAL DE CORONACIÓN
# ---------------------------------------------------------

def dibujar_modal_coronacion(pantalla, estado):
    import pygame
    from nucleo.cargador_piezas import cargar_imagen_pieza

    overlay = pygame.Surface((ANCHO_TABLERO, ALTO_TABLERO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))
    pantalla.blit(overlay, (0, 0))

    piezas = ["Q", "R", "B", "N"]

    for i, rect in enumerate(estado.rects_coronacion):
        pygame.draw.rect(pantalla, (240, 240, 240), rect)
        pygame.draw.rect(pantalla, (0, 0, 0), rect, 3)

        # Cargar imagen de pieza blanca (modo LEER siempre promueve blancas)
        imagen = cargar_imagen_pieza(piezas[i])

        # Centrar imagen dentro del rectángulo
        ix = rect.x + (rect.width - imagen.get_width()) // 2
        iy = rect.y + (rect.height - imagen.get_height()) // 2

        pantalla.blit(imagen, (ix, iy))
