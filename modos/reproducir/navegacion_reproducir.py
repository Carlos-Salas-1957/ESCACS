import pygame

from nucleo.tablero import dibujar_tablero, dibujar_piezas
from nucleo.panel_jugadas import dibujar_panel_jugadas

from modos.reproducir.botones_reproducir import dibujar_botones_reproducir



def dibujar_navegacion_reproducir(pantalla):
    fuente = pygame.font.SysFont("arial", 28)

    x_panel = 512
    y = 384  # franja 384–448

    ancho_panel = 240
    margen = 16
    espacio_util = ancho_panel - margen * 2
    ancho_boton = espacio_util // 4   # cuatro botones repartidos

    textos = ["<<", "<", ">", ">>"]

    for i, texto in enumerate(textos):
        x = x_panel + margen + i * ancho_boton

        pygame.draw.rect(pantalla, (80, 80, 80), (x, y, ancho_boton - 4, 64))

        label = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(
            label,
            (x + (ancho_boton - 4)//2 - label.get_width()//2,
             y + 18)
        )
