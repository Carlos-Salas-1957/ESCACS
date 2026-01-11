def manejar_click_tablero(estado, x, y):
    # Aquí irá la lógica de seleccionar pieza y mover
    pass

def deshacer(estado):
    if not estado.historial:
        return
    estado.posicion = estado.historial.pop()

def cambiar_color(estado):
    estado.orientacion = "invertida" if estado.orientacion == "normal" else "normal"
