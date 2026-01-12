import pygame

def dibujar_botones_estudiar(pantalla):
    fuente = pygame.font.SysFont("arial", 20)

    botones = [
        ("COLOR", 640),
        ("CARGAR", 720),
        ("INFO", 800),
    ]

    y = 448
    for texto, x in botones:
        pygame.draw.rect(pantalla, (80, 80, 80), (x, y, 80, 64))
        label = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(label, (x + 40 - label.get_width() // 2, y + 22))
