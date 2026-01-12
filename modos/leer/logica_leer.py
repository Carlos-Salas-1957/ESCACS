import chess
from nucleo.tablero import casilla_desde_pixel
from modos.leer.coronacion import ventana_coronacion, letra_promocion


# ---------------------------------------------------------
# Asegurar tablero interno
# ---------------------------------------------------------
def _asegurar_tablero(estado):
    if not hasattr(estado, "tablero_chess") or estado.tablero_chess is None:
        estado.tablero_chess = chess.Board()


# ---------------------------------------------------------
# Elegir pieza de coronación (UI modal)
# ---------------------------------------------------------
def _elegir_pieza_coronacion(estado, color):
    return ventana_coronacion(estado.pantalla, color)


# ---------------------------------------------------------
# Construir UCI (incluye coronación)
# ---------------------------------------------------------
def _construir_uci(estado, origen, destino):
    _asegurar_tablero(estado)

    sq_origen = chess.parse_square(origen)
    pieza = estado.tablero_chess.piece_at(sq_origen)

    # ¿Es coronación?
    if pieza and pieza.piece_type == chess.PAWN and destino[1] in "18":
        color = "w" if pieza.color == chess.WHITE else "b"
        promo = _elegir_pieza_coronacion(estado, color)

        if promo is None:
            return None

        return f"{origen}{destino}{promo}"

    return f"{origen}{destino}"


# ---------------------------------------------------------
# Aplicar movimiento visual (tu representación)
# ---------------------------------------------------------
def _aplicar_movimiento_visual(estado, mov, origen, destino, es_enroque, es_en_passant):
    pieza = estado.posicion.pop(origen, None)
    if pieza is None:
        return

    estado.posicion[destino] = pieza

    # -------------------------
    # ENROQUE VISUAL
    # -------------------------
    if es_enroque:
        # Blancas
        if origen == "e1" and destino == "g1":
            if "h1" in estado.posicion:
                estado.posicion["f1"] = estado.posicion.pop("h1")

        elif origen == "e1" and destino == "c1":
            if "a1" in estado.posicion:
                estado.posicion["d1"] = estado.posicion.pop("a1")

        # Negras
        elif origen == "e8" and destino == "g8":
            if "h8" in estado.posicion:
                estado.posicion["f8"] = estado.posicion.pop("h8")

        elif origen == "e8" and destino == "c8":
            if "a8" in estado.posicion:
                estado.posicion["d8"] = estado.posicion.pop("a8")

    # -------------------------
    # CAPTURA AL PASO (detectada ANTES del push)
    # -------------------------
    if es_en_passant:
        destino_sq = chess.parse_square(destino)

        # Color de la pieza que acaba de mover (NO usar turno)
        pieza_movida = estado.tablero_chess.piece_at(destino_sq)
        color_blancas = pieza_movida.color == chess.WHITE

        # Blancas capturan hacia arriba, negras hacia abajo
        if color_blancas:
            capturada_sq = destino_sq - 8
        else:
            capturada_sq = destino_sq + 8

        capturada_alg = chess.square_name(capturada_sq)

        if capturada_alg in estado.posicion:
            estado.posicion.pop(capturada_alg)

    # -------------------------
    # CORONACIÓN VISUAL
    # -------------------------
    if mov.promotion:
        cod = estado.posicion[destino]
        letra = letra_promocion(mov.promotion)
        estado.posicion[destino] = cod[0] + letra


# ---------------------------------------------------------
# Manejar clic en tablero
# ---------------------------------------------------------
def manejar_click_tablero(estado, x, y):
    _asegurar_tablero(estado)

    casilla = casilla_desde_pixel(x, y, estado.orientacion)
    if casilla is None:
        return

    # Selección inicial
    if estado.seleccion is None:
        if casilla in estado.posicion:
            estado.seleccion = casilla
        return

    origen = estado.seleccion
    destino = casilla

    # Deselección
    if origen == destino:
        estado.seleccion = None
        return

    # Construir UCI
    uci = _construir_uci(estado, origen, destino)
    if uci is None:
        estado.seleccion = None
        return

    mov = chess.Move.from_uci(uci)

    # Movimiento ilegal
    if mov not in estado.tablero_chess.legal_moves:
        estado.seleccion = None
        return

    # Detectar enroque y en‑passant ANTES del push
    es_enroque = estado.tablero_chess.is_castling(mov)
    es_en_passant = estado.tablero_chess.is_en_passant(mov)

    # Guardar estado para UNDO
    estado.historial.append((
        estado.posicion.copy(),
        [j[:] for j in estado.jugadas],
        estado.turno,
        estado.tablero_chess.fen()
    ))

    # SAN antes del push
    san = estado.tablero_chess.san(mov)

    # Aplicar en motor
    estado.tablero_chess.push(mov)

    # Aplicar visual
    _aplicar_movimiento_visual(estado, mov, origen, destino, es_enroque, es_en_passant)

    # Registrar jugada
    if estado.turno == "blancas":
        estado.jugadas.append([len(estado.jugadas) + 1, san, ""])
        estado.turno = "negras"
    else:
        estado.jugadas[-1][2] = san
        estado.turno = "blancas"

    estado.ultima_jugada = (origen, destino)
    estado.seleccion = None


# ---------------------------------------------------------
# UNDO
# ---------------------------------------------------------
def deshacer(estado):
    if not estado.historial:
        return

    pos, jug, turno, fen = estado.historial.pop()

    estado.posicion = pos
    estado.jugadas = jug
    estado.turno = turno

    if hasattr(estado, "tablero_chess") and estado.tablero_chess is not None:
        estado.tablero_chess.set_fen(fen)

    estado.seleccion = None
    estado.ultima_jugada = None


# ---------------------------------------------------------
# Cambiar orientación
# ---------------------------------------------------------
def cambiar_color(estado):
    estado.orientacion = "invertida" if estado.orientacion == "normal" else "normal"
