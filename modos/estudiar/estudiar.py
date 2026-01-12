import pygame
import chess

from modos.estudiar.estado_estudiar import EstadoEstudiar
from modos.estudiar.interfaz_estudiar import dibujar_interfaz_estudiar
from modos.estudiar.logica_estudiar import manejar_eventos_estudiar


def ejecutar_estudiar(pantalla):
    estado = EstadoEstudiar(chess.Board())
    reloj = pygame.time.Clock()

    while estado.ejecutando:
        for evento in pygame.event.get():
            manejar_eventos_estudiar(evento, estado)

        dibujar_interfaz_estudiar(pantalla, estado)
        pygame.display.flip()
        reloj.tick(60)
