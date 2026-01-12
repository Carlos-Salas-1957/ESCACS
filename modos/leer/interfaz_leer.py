import pygame
from nucleo.tablero import dibujar_tablero, dibujar_piezas
from nucleo.panel_jugadas import dibujar_panel_jugadas


def dibujar_interfaz_leer(pantalla, estado):
    pantalla.fill((30, 30, 30))

    # Tablero + piezas (tu versión)
    dibujar_tablero(pantalla)
    dibujar_piezas(pantalla, estado.tablero)

    # Panel lateral
    dibujar_panel_lateral_leer(pantalla)
    dibujar_panel_jugadas(pantalla, estado, 512, 80, 240, 480)
    dibujar_botones_leer(pantalla)


def dibujar_panel_lateral_leer(pantalla):
    pygame.draw.rect(pantalla, (50, 50, 50), (512, 0, 240, 512))

    fuente = pygame.font.SysFont("arial", 24)
    texto = fuente.render("MODO LEER", True, (255, 255, 255))
    pantalla.blit(texto, (512 + 16, 24))


def dibujar_botones_leer(pantalla):
    fuente = pygame.font.SysFont("arial", 18)

    botones = [("COLOR", 0), ("DESHACER", 1), ("SALIR", 2)]
    for texto, i in botones:
        x = 512 + i * 80
        y = 560
        pygame.draw.rect(pantalla, (60, 60, 60), (x, y, 80, 50))
        pygame.draw.rect(pantalla, (100, 100, 100), (x, y, 80, 50), 2)

        txt = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(txt, (x + 10, y + 14))
