import pygame
from modos.leer.estado_leer import EstadoLeer
from modos.leer.interfaz_leer import dibujar_interfaz_leer, manejar_botones_leer
from modos.leer.logica_leer import manejar_click_tablero

def modo_leer(pantalla):
    reloj = pygame.time.Clock()
    estado = EstadoLeer()

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if manejar_botones_leer(estado, x, y):
                    ejecutando = False
                else:
                    manejar_click_tablero(estado, x, y)

        dibujar_interfaz_leer(pantalla, estado)
        pygame.display.flip()
        reloj.tick(60)
