import pygame
import chess

from modos.reproducir.estado_reproducir import EstadoReproducir
from modos.reproducir.interfaz_reproducir import dibujar_interfaz_reproducir
from modos.reproducir.logica_reproducir import manejar_eventos_reproducir


def ejecutar_reproducir(pantalla, movimientos):
    estado = EstadoReproducir(chess.Board(), movimientos)
    reloj = pygame.time.Clock()

    while estado.ejecutando:
        for evento in pygame.event.get():
            manejar_eventos_reproducir(evento, estado)

        dibujar_interfaz_reproducir(pantalla, estado)
        pygame.display.flip()
        reloj.tick(60)
