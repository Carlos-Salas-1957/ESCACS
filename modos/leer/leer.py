import pygame
import chess

from modos.leer.estado_leer import EstadoLeer
from modos.leer.interfaz_leer import dibujar_interfaz_leer
from modos.leer.logica_leer import manejar_eventos_leer


def ejecutar_leer(pantalla):
    estado = EstadoLeer(chess.Board())
    reloj = pygame.time.Clock()

    while estado.ejecutando:
        for evento in pygame.event.get():
            manejar_eventos_leer(evento, estado)

        dibujar_interfaz_leer(pantalla, estado)
        pygame.display.flip()
        reloj.tick(60)
