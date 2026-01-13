import pygame

class Boton:
    def __init__(self, texto, x, y, ancho, alto):
        self.texto = texto
        self.rect = pygame.Rect(x, y, ancho, alto)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (100, 100, 100), self.rect)
        fuente = pygame.font.SysFont("arial", 24)
        txt = fuente.render(self.texto, True, (255, 255, 255))
        pantalla.blit(txt, (self.rect.x + 10, self.rect.y + 10))

    def pulsado(self):
        return (
            self.rect.collidepoint(pygame.mouse.get_pos())
            and pygame.mouse.get_pressed()[0]
        )
