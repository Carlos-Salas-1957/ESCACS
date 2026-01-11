from nucleo.constantes import TAM_CASILLA, ANCHO_TABLERO, ALTO_TABLERO

# ============================
# ¿Está el clic dentro del tablero?
# ============================

def dentro_tablero(x, y):
    return 0 <= x < ANCHO_TABLERO and 0 <= y < ALTO_TABLERO


# ============================
# Convertir pixel → casilla ("e4")
# ============================

def casilla_desde_pixel(x, y, orientacion="normal"):
    if not dentro_tablero(x, y):
        return None

    col = x // TAM_CASILLA
    fila = y // TAM_CASILLA

    if orientacion == "invertida":
        col = 7 - col
        fila = 7 - fila

    letra = chr(ord("a") + col)
    numero = str(8 - fila)

    return letra + numero


# ============================
# Convertir casilla ("e4") → pixel (x, y)
# ============================

def pixel_desde_casilla(casilla, orientacion="normal"):
    col = ord(casilla[0]) - ord("a")
    fila = 8 - int(casilla[1])

    if orientacion == "invertida":
        col = 7 - col
        fila = 7 - fila

    x = col * TAM_CASILLA
    y = fila * TAM_CASILLA

    return x, y
