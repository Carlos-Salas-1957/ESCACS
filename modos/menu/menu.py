import pygame

from modos.menu.estado_menu import EstadoMenu
from modos.menu.interfaz_menu import dibujar_interfaz_menu
from modos.menu.logica_menu import manejar_eventos_menu


def ejecutar_menu(pantalla):
    estado = EstadoMenu()
    reloj = pygame.time.Clock()

    while estado.ejecutando:
        for evento in pygame.event.get():
            accion = manejar_eventos_menu(evento, estado)

            if accion is not None:
                return accion   # ← DEVOLVEMOS LA ACCIÓN AL PRINCIPAL

        dibujar_interfaz_menu(pantalla, estado)
        pygame.display.flip()
        reloj.tick(60)
