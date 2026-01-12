import pygame
import os
from nucleo.constantes import RUTA_PIEZAS, TAM_CASILLA

_cache_piezas = {}

MAPA_PIEZAS = {
    "p": "bp.png",
    "r": "br.png",
    "n": "bn.png",
    "b": "bb.png",
    "q": "bq.png",
    "k": "bk.png",
    "P": "wp.png",
    "R": "wr.png",
    "N": "wn.png",
    "B": "wb.png",
    "Q": "wq.png",
    "K": "wk.png",
}

def cargar_imagen_pieza(simbolo):
    if simbolo in _cache_piezas:
        return _cache_piezas[simbolo]

    nombre_archivo = MAPA_PIEZAS[simbolo]
    carpeta = os.path.join(*RUTA_PIEZAS)
    ruta = os.path.join(carpeta, nombre_archivo)

    imagen = pygame.image.load(ruta).convert_alpha()
    imagen = pygame.transform.scale(imagen, (TAM_CASILLA, TAM_CASILLA))

    _cache_piezas[simbolo] = imagen
    return imagen
