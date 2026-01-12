import pygame

from nucleo.tablero import dibujar_tablero, dibujar_piezas
from nucleo.panel_jugadas import dibujar_panel_jugadas

from modos.reproducir.navegacion_reproducir import dibujar_navegacion_reproducir
from modos.reproducir.botones_reproducir import dibujar_botones_reproducir


def dibujar_interfaz_reproducir(pantalla, estado):
    pantalla.fill((30, 30, 30))

    # -------------------------
    # TABLERO (512x512)
    # -------------------------
    dibujar_tablero(pantalla)
    dibujar_piezas(pantalla, estado.tablero)

    # -------------------------
    # PANEL LATERAL (512 px)
    # -------------------------
    pygame.draw.rect(pantalla, (50, 50, 50), (512, 0, 240, 512))

    # -------------------------
    # 0–64: TÍTULO DEL MODO
    # -------------------------
    fuente = pygame.font.SysFont("arial", 32)
    texto = fuente.render("MODO REPRODUCIR", True, (255, 255, 255))
    pantalla.blit(texto, (512 + 120 - texto.get_width() // 2, 16))

    # -------------------------
    # 64–384: PANEL DE JUGADAS
    # -------------------------
    dibujar_panel_jugadas(
        pantalla,
        estado,
        x=512,
        y=64,
        ancho=240,
        alto=320
    )

    # -------------------------
    # 384–448: NAVEGACIÓN
    # -------------------------
    dibujar_navegacion_reproducir(pantalla)

    # -------------------------
    # 448–512: BOTONES DEL MODO
    # -------------------------
    dibujar_botones_reproducir(pantalla)
