import pygame
import chess
from nucleo.cargador_piezas import cargar_piezas

# ---------------------------------------------------------
# Cargar imágenes de piezas
# ---------------------------------------------------------
piezas_img = cargar_piezas()

# ---------------------------------------------------------
# Mapeo python-chess → letra UCI
# ---------------------------------------------------------
MAPA_PROMO = {
    chess.KNIGHT: "n",
    chess.BISHOP: "b",
    chess.ROOK:   "r",
    chess.QUEEN:  "q"
}

def letra_promocion(tipo):
    """
    Convierte el número de promoción de python-chess
    (2,3,4,5) en letra UCI ('n','b','r','q').
    """
    return MAPA_PROMO.get(tipo, "q")  # seguridad: por defecto dama

# ---------------------------------------------------------
# Ventana modal de coronación
# ---------------------------------------------------------
def ventana_coronacion(pantalla, color):
    """
    Muestra una ventana modal con 4 piezas para elegir coronación.
    color = 'w' o 'b'
    Devuelve: 'q', 'r', 'b', 'n'
    """

    ancho = 300
    alto = 150
    x = (pantalla.get_width() - ancho) // 2
    y = (pantalla.get_height() - alto) // 2

    rect_popup = pygame.Rect(x, y, ancho, alto)

    piezas = ["q", "r", "b", "n"]
    botones = {}

    # Crear botones para cada pieza
    for i, p in enumerate(piezas):
        bx = x + 20 + i * 70
        by = y + 50
        botones[p] = pygame.Rect(bx, by, 64, 64)

    # Bucle modal
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None

            if evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = evento.pos
                for p, rect in botones.items():
                    if rect.collidepoint(mx, my):
                        return p

        # Dibujar popup
        pygame.draw.rect(pantalla, (240, 240, 240), rect_popup)
        pygame.draw.rect(pantalla, (0, 0, 0), rect_popup, 3)

        # Título
        fuente = pygame.font.SysFont("Arial", 24)
        txt = fuente.render("Elige pieza de coronación", True, (0, 0, 0))
        pantalla.blit(txt, (x + 20, y + 10))

        # Dibujar piezas
        for p, rect in botones.items():
            clave = color + p  # ej: 'wq', 'br'
            img = piezas_img.get(clave)
            if img:
                pantalla.blit(img, rect.topleft)

        pygame.display.flip()
