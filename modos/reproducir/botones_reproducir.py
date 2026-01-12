import pygame

def dibujar_botones_reproducir(pantalla):
    fuente = pygame.font.SysFont("arial", 24)

    # Panel lateral empieza en x = 512
    x_panel = 512
    y = 448  # franja 448–512

    ancho_panel = 240
    margen = 16
    espacio_util = ancho_panel - margen * 2
    ancho_boton = espacio_util // 3   # tres botones repartidos

    textos = ["COLOR", "CARGAR", "INFO"]

    for i, texto in enumerate(textos):
        x = x_panel + margen + i * ancho_boton

        # Dibujar botón
        pygame.draw.rect(pantalla, (80, 80, 80), (x, y, ancho_boton - 4, 64))

        # Texto centrado
        label = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(
            label,
            (x + (ancho_boton - 4)//2 - label.get_width()//2,
             y + 20)
        )
