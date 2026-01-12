import pygame
from modos.menu.menu import ejecutar_menu
from modos.leer.leer import ejecutar_leer
from modos.estudiar.estudiar import ejecutar_estudiar
from modos.reproducir.reproducir import ejecutar_reproducir

pygame.init()
pantalla = pygame.display.set_mode((752, 512))
pygame.display.set_caption("ESCACS")

modo = ejecutar_menu(pantalla)

if modo == "leer":
    ejecutar_leer(pantalla)

elif modo == "estudiar":
    ejecutar_estudiar(pantalla)

elif modo == "reproducir":
    # Aquí REPRODUCIR necesita movimientos
    # De momento, lista vacía o de prueba
    movimientos = []
    ejecutar_reproducir(pantalla, movimientos)

pygame.quit()
