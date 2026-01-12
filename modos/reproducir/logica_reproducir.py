import pygame
import chess
import chess.pgn
from tkinter import Tk, filedialog


# ---------------------------------------------------------
# CARGAR PARTIDA (PGN)
# ---------------------------------------------------------
def cargar_partida(estado):
    Tk().withdraw()  # Ocultar ventana Tk

    ruta = filedialog.askopenfilename(
        title="Seleccionar partida PGN",
        filetypes=[("Archivos PGN", "*.pgn")]
    )

    if not ruta:
        return

    with open(ruta, "r", encoding="utf-8") as f:
        partida = chess.pgn.read_game(f)

    # Guardar info de la partida
    estado.evento = partida.headers.get("Event", "")
    estado.blancas = partida.headers.get("White", "")
    estado.negras = partida.headers.get("Black", "")
    estado.fecha = partida.headers.get("Date", "")
    estado.resultado = partida.headers.get("Result", "")

    # Extraer movimientos python-chess
    movimientos = []
    nodo = partida

    while nodo.variations:
        nodo = nodo.variations[0]
        movimientos.append(nodo.move)

    # Reiniciar estado
    estado.tablero = chess.Board()
    estado.movimientos = movimientos
    estado.indice = -1


# ---------------------------------------------------------
# MOSTRAR INFO DE LA PARTIDA
# ---------------------------------------------------------
def mostrar_info(estado):
    print("\n--- INFORMACIÓN DE LA PARTIDA ---")
    print("Evento:", estado.evento)
    print("Blancas:", estado.blancas)
    print("Negras:", estado.negras)
    print("Fecha:", estado.fecha)
    print("Resultado:", estado.resultado)
    print("---------------------------------\n")


# ---------------------------------------------------------
# NAVEGACIÓN ENTRE JUGADAS
# ---------------------------------------------------------
def avanzar(estado):
    if estado.indice + 1 < len(estado.movimientos):
        estado.indice += 1
        estado.tablero.push(estado.movimientos[estado.indice])


def retroceder(estado):
    if estado.indice >= 0:
        estado.tablero.pop()
        estado.indice -= 1


def ir_inicio(estado):
    while estado.indice >= 0:
        estado.tablero.pop()
        estado.indice -= 1


def ir_final(estado):
    while estado.indice + 1 < len(estado.movimientos):
        estado.indice += 1
        estado.tablero.push(estado.movimientos[estado.indice])


# ---------------------------------------------------------
# DETECCIÓN DE CLICS EN BOTONES
# ---------------------------------------------------------
def manejar_eventos_reproducir(evento, estado):
    if evento.type == pygame.QUIT:
        estado.ejecutando = False

    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        x, y = evento.pos

        # -------------------------------------------------
        # BOTONES DE NAVEGACIÓN (384–448)
        # -------------------------------------------------
        if 384 <= y <= 448:
            # << (ir al inicio)
            if 512 + 16 <= x < 512 + 16 + 56:
                ir_inicio(estado)

            # < (retroceder)
            elif 512 + 16 + 56 <= x < 512 + 16 + 112:
                retroceder(estado)

            # > (avanzar)
            elif 512 + 16 + 112 <= x < 512 + 16 + 168:
                avanzar(estado)

            # >> (ir al final)
            elif 512 + 16 + 168 <= x < 512 + 16 + 224:
                ir_final(estado)

        # -------------------------------------------------
        # BOTONES DEL MODO (448–512)
        # -------------------------------------------------
        if 448 <= y <= 512:
            # COLOR
            if 512 + 16 <= x < 512 + 16 + 70:
                estado.tablero = estado.tablero.mirror()

            # CARGAR
            elif 512 + 16 + 80 <= x < 512 + 16 + 150:
                cargar_partida(estado)

            # INFO
            elif 512 + 16 + 160 <= x < 512 + 16 + 230:
                mostrar_info(estado)
