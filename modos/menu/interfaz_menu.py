import pygame

from modos.menu.botones_menu import dibujar_botones_menu


def dibujar_interfaz_menu(pantalla, estado):
    pantalla.fill((30, 30, 30))

    # Título centrado
    fuente = pygame.font.SysFont("arial", 48)
    texto = fuente.render("ESCACS", True, (255, 255, 255))
    pantalla.blit(texto, (320 - texto.get_width() // 2, 80))

    # Botones
    dibujar_botones_menu(pantalla)
