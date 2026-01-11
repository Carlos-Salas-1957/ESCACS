import pygame
import sys

from nucleo.constantes import *
from modos.leer.leer import modo_leer


# ============================
# INICIALIZACIÓN
# ============================

def iniciar_pygame():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("ESCACS")
    return pantalla


# ============================
# MENÚ PRINCIPAL
# ============================

def menu_principal(pantalla):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Arial", 36)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    modo_leer(pantalla)     # ← ENTRAR EN MODO LEER
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pantalla.fill((50, 50, 50))

        texto1 = fuente.render("1 - Modo LEER", True, (255, 255, 255))
        texto2 = fuente.render("ESC - Salir", True, (255, 255, 255))

        pantalla.blit(texto1, (50, 100))
        pantalla.blit(texto2, (50, 160))

        pygame.display.flip()
        reloj.tick(60)


# ============================
# PROGRAMA PRINCIPAL
# ============================

def main():
    pantalla = iniciar_pygame()
    menu_principal(pantalla)


if __name__ == "__main__":
    main()
