from nucleo.tablero import casilla_desde_pixel

def manejar_click_tablero(estado, x, y):
    casilla = casilla_desde_pixel(x, y, estado.orientacion)
    if casilla is None:
        return

    # primera pulsación: seleccionar
    if estado.seleccion is None:
        if casilla in estado.posicion:
            estado.seleccion = casilla
        return

    origen = estado.seleccion
    destino = casilla

    # misma casilla → deseleccionar
    if origen == destino:
        estado.seleccion = None
        return

    # guardar posición para UNDO
    estado.historial.append(estado.posicion.copy())

    # mover pieza (sin reglas)
    pieza = estado.posicion.pop(origen)
    estado.posicion[destino] = pieza

    mov = f"{origen}-{destino}"

    if estado.turno == "blancas":
        estado.jugadas.append([len(estado.jugadas) + 1, mov, ""])
        estado.turno = "negras"
    else:
        estado.jugadas[-1][2] = mov
        estado.turno = "blancas"

    estado.ultima_jugada = (origen, destino)
    estado.seleccion = None

def deshacer(estado):
    if not estado.historial:
        return
    estado.posicion = estado.historial.pop()
    estado.seleccion = None
    if estado.jugadas:
        num, bl, ng = estado.jugadas[-1]
        if ng:
            estado.jugadas[-1][2] = ""
            estado.turno = "negras"
        else:
            estado.jugadas.pop()
            estado.turno = "blancas"
    estado.ultima_jugada = None

def cambiar_color(estado):
    estado.orientacion = "invertida" if estado.orientacion == "normal" else "normal"
