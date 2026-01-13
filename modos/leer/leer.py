import pygame
import chess

from modos.leer.estado_leer import EstadoLeer
from modos.leer.interfaz_leer import dibujar_interfaz_leer
from modos.leer.eventos_leer import manejar_eventos_leer

def ejecutar_leer(pantalla):
    estado = EstadoLeer()
    reloj = pygame.time.Clock()

    while estado.ejecutando:
        accion = manejar_eventos_leer(estado)
        if accion == "salir":
            estado.ejecutando = False

        dibujar_interfaz_leer(pantalla, estado)
        pygame.display.flip()
        reloj.tick(60)

