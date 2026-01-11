import pygame
from nucleo.cargador_piezas import cargar_piezas
from nucleo.constantes import (
    TAM_CASILLA, COLOR_CLARO, COLOR_OSCURO, COLOR_FONDO_PANEL,
    ANCHO_TABLERO
)
from nucleo.tablero import pixel_desde_casilla
from modos.leer.logica_leer import manejar_click_tablero, deshacer, cambiar_color

# Si no existen fuera, los fijamos aquí
ALTO_TABLERO = 8 * TAM_CASILLA
ANCHO_PANEL = 240

piezas_img = cargar_piezas()

# Layout panel
ALT_NOMBRE = 64
ALT_CAB = 32
ALT_BOT = 64
Y_NOMBRE = 0
Y_CAB = Y_NOMBRE + ALT_NOMBRE
Y_JUG = Y_CAB + ALT_CAB
ALT_JUG = ALTO_TABLERO - Y_JUG - ALT_BOT
Y_BOT = ALTO_TABLERO - ALT_BOT

# Botones con coordenadas absolutas
BOTON_UNDO  = pygame.Rect(ANCHO_TABLERO + 10,  Y_BOT + 12, 70, 40)
BOTON_COLOR = pygame.Rect(ANCHO_TABLERO + 85,  Y_BOT + 12, 80, 40)
BOTON_SALIR = pygame.Rect(ANCHO_TABLERO + 170, Y_BOT + 12, 70, 40)

COLOR_SELECCION = (255, 255, 0)

def dibujar_tablero(pantalla):
    colores = [COLOR_CLARO, COLOR_OSCURO]
    for f in range(8):
        for c in range(8):
            pygame.draw.rect(
                pantalla,
                colores[(f + c) % 2],
                (c * TAM_CASILLA, f * TAM_CASILLA, TAM_CASILLA, TAM_CASILLA)
            )

def dibujar_piezas(pantalla, estado):
    for casilla, pieza in estado.posicion.items():
        x, y = pixel_desde_casilla(casilla, estado.orientacion)
        img = piezas_img.get(pieza)
        if img:
            pantalla.blit(img, (x, y))

def dibujar_jugadas(pantalla, estado):
    fuente = pygame.font.SysFont("Arial", 20)
    x_num = ANCHO_TABLERO + 8
    x_bl  = ANCHO_TABLERO + 40
    x_ng  = ANCHO_TABLERO + 140
    fila_h = 22
    max_filas = ALT_JUG // fila_h
    jug = estado.jugadas
    ini = max(0, len(jug) - max_filas)
    for i in range(ini, len(jug)):
        num, bl, ng = jug[i]
        y = Y_JUG + (i - ini) * fila_h + 2
        pantalla.blit(fuente.render(f"{num:>3}.", True, (0, 0, 0)), (x_num, y))
        pantalla.blit(fuente.render(bl, True, (0, 0, 0)), (x_bl, y))
        pantalla.blit(fuente.render(ng, True, (0, 0, 0)), (x_ng, y))

def dibujar_panel_lateral(pantalla, estado):
    pygame.draw.rect(pantalla, COLOR_FONDO_PANEL,
                     (ANCHO_TABLERO, 0, ANCHO_PANEL, ALTO_TABLERO))

    f_tit = pygame.font.SysFont("Arial", 28)
    f_cab = pygame.font.SysFont("Arial", 22)
    f_btn = pygame.font.SysFont("Arial", 20)

    pantalla.blit(f_tit.render("MODO LEER", True, (0, 0, 0)),
                  (ANCHO_TABLERO + 20, Y_NOMBRE + 18))

    pygame.draw.rect(pantalla, (210, 210, 210),
                     (ANCHO_TABLERO, Y_CAB, ANCHO_PANEL, ALT_CAB))
    pantalla.blit(f_cab.render("#", True, (0, 0, 0)),
                  (ANCHO_TABLERO + 8, Y_CAB + 6))
    pantalla.blit(f_cab.render("Blancas", True, (0, 0, 0)),
                  (ANCHO_TABLERO + 40, Y_CAB + 6))
    pantalla.blit(f_cab.render("Negras", True, (0, 0, 0)),
                  (ANCHO_TABLERO + 140, Y_CAB + 6))

    pygame.draw.rect(pantalla, (230, 230, 230),
                     (ANCHO_TABLERO, Y_JUG, ANCHO_PANEL, ALT_JUG))
    dibujar_jugadas(pantalla, estado)

    pygame.draw.rect(pantalla, (200, 200, 200),
                     (ANCHO_TABLERO, Y_BOT, ANCHO_PANEL, ALT_BOT))

    pygame.draw.rect(pantalla, (180, 180, 180), BOTON_UNDO)
    pygame.draw.rect(pantalla, (180, 180, 180), BOTON_COLOR)
    pygame.draw.rect(pantalla, (180, 180, 180), BOTON_SALIR)

    pantalla.blit(f_btn.render("UNDO", True, (0, 0, 0)),
                  (BOTON_UNDO.x + 8, BOTON_UNDO.y + 10))
    pantalla.blit(f_btn.render("COLOR", True, (0, 0, 0)),
                  (BOTON_COLOR.x + 8, BOTON_COLOR.y + 10))
    pantalla.blit(f_btn.render("SALIR", True, (0, 0, 0)),
                  (BOTON_SALIR.x + 8, BOTON_SALIR.y + 10))

def dibujar_interfaz_leer(pantalla, estado):
    pantalla.fill(COLOR_FONDO_PANEL)
    dibujar_tablero(pantalla)
    dibujar_piezas(pantalla, estado)

    if estado.ultima_jugada:
        o, d = estado.ultima_jugada
        for cas in (o, d):
            x, y = pixel_desde_casilla(cas, estado.orientacion)
            pygame.draw.rect(pantalla, (255, 200, 0),
                             (x, y, TAM_CASILLA, TAM_CASILLA), 4)

    if estado.seleccion:
        x, y = pixel_desde_casilla(estado.seleccion, estado.orientacion)
        pygame.draw.rect(pantalla, COLOR_SELECCION,
                         (x, y, TAM_CASILLA, TAM_CASILLA), 4)

    dibujar_panel_lateral(pantalla, estado)

def manejar_eventos_leer(estado, evento):
    if evento.type == pygame.MOUSEBUTTONDOWN:
        x, y = evento.pos

        if BOTON_UNDO.collidepoint(x, y):
            deshacer(estado)
            return False
        if BOTON_COLOR.collidepoint(x, y):
            cambiar_color(estado)
            return False
        if BOTON_SALIR.collidepoint(x, y):
            return True

        if x < ANCHO_TABLERO:
            manejar_click_tablero(estado, x, y)

    return False
