import pygame
from modos.leer.estado_leer import EstadoLeer
from modos.leer.interfaz_leer import dibujar_interfaz_leer, manejar_eventos_leer

def modo_leer(pantalla):
    reloj = pygame.time.Clock()
    estado = EstadoLeer()

    estado.pantalla = pantalla  # NECESARIO PARA LA VENTANA DE CORONACIÓN

    salir = False
    while not salir:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return
            salir = manejar_eventos_leer(estado, evento)

        dibujar_interfaz_leer(pantalla, estado)
        pygame.display.flip()
        reloj.tick(60)
