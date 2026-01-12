import pygame

def dibujar_botones_menu(pantalla):
    fuente = pygame.font.SysFont("arial", 32)

    botones = [
        ("LEER", 180),
        ("REPRODUCIR", 250),
        ("ESTUDIAR", 320),
        ("SALIR", 390),
    ]

    for texto, y in botones:
        pygame.draw.rect(pantalla, (80, 80, 80), (200, y, 240, 50))
        label = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(label, (200 + 120 - label.get_width() // 2, y + 10))
