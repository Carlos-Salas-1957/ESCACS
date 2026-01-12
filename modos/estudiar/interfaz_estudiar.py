import pygame

from nucleo.tablero import dibujar_tablero, dibujar_piezas
from nucleo.panel_jugadas import dibujar_panel_jugadas
from modos.estudiar.botones_estudiar import dibujar_botones_estudiar


def dibujar_interfaz_estudiar(pantalla, estado):
    pantalla.fill((30, 30, 30))

    # Tablero
    dibujar_tablero(pantalla)
    dibujar_piezas(pantalla, estado.tablero)

    # Panel lateral
    pygame.draw.rect(pantalla, (50, 50, 50), (640, 0, 240, 512))

    # Título (0–64)
    fuente = pygame.font.SysFont("arial", 32)
    texto = fuente.render("MODO ESTUDIAR", True, (255, 255, 255))
    pantalla.blit(texto, (650, 15))

    # Panel de jugadas (64–384)
    dibujar_panel_jugadas(pantalla, estado, x=640, y=64, ancho=240, alto=320)

    # Botones (448–512)
    dibujar_botones_estudiar(pantalla)
