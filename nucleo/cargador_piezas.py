import pygame
import os
from nucleo.constantes import RUTA_PIEZAS

def cargar_piezas():
    piezas = {}
    ruta = os.path.join(*RUTA_PIEZAS)

    for archivo in os.listdir(ruta):
        if archivo.endswith(".png"):
            nombre = archivo.split(".")[0].lower()  # wP → wp
            piezas[nombre] = pygame.image.load(os.path.join(ruta, archivo))

    return piezas
