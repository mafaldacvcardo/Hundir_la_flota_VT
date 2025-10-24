import numpy as np
import random

def crear_tablero(tamaño=10):
    tablero = np.full((tamaño, tamaño), "_")
    return tablero

def mostrar_tablero(tablero, ocultar_barcos=False):
    for fila in tablero:
        fila_mostrar = []
        for casilla in fila:
            if ocultar_barcos and casilla == "O":
                fila_mostrar.append("_")
            else:
                fila_mostrar.append(casilla)
        print(" ".join(fila_mostrar))

def crear_barco(eslora, tamaño_tablero=10):
    horizontal = random.choice([True, False])
    if horizontal:
        fila = random.randint(0, tamaño_tablero - 1)
        columna_inicio = random.randint(0, tamaño_tablero - eslora)
        barco = [(fila, columna_inicio + i) for i in range(eslora)]
    else:
        columna = random.randint(0, tamaño_tablero - 1)
        fila_inicio = random.randint(0, tamaño_tablero - eslora)
        barco = [(fila_inicio + i, columna) for i in range(eslora)]
    return barco

def generar_barcos_aleatorios(tablero, lista_esloras):
    barcos = []
    for eslora in lista_esloras:
        while True:
            barco = crear_barco(eslora, tamaño_tablero=10)
            barco_valido = True
            for f, c in barco:
                if tablero[f, c] != "_":
                    barco_valido = False
                    break
            if barco_valido:
                colocar_barcos(barco, tablero)
                barcos.append(barco)
                break      
    return barcos

def colocar_barcos(barco, tablero):
    for (fila, columna) in barco:
        tablero[fila, columna] = "O"


def disparar(casilla, tablero, barcos):
    fila, columna = casilla
    if tablero[fila, columna] == "O":
        tablero[fila, columna] = "X"
        print("¡Tocado!")
        for barco in barcos:
            if barco_hundido(barco, tablero):
                print("¡Hundido!")
                barcos.remove(barco)
                break
        return "tocado"
    elif tablero[fila, columna] == "_":
        tablero[fila, columna] = "*"
        print("¡Agua!")
        return "agua"
    else:
        print("¡Ya disparaste ahí antes!")
        return "repetido"

def barco_hundido(barco, tablero):
    for f, c in barco:
        if tablero[f, c] != "X":
            return False
    return True


def todos_hundidos(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == "O":
                return False
    return True

def turno_jugador(tablero_maquina, barcos_maquina):
    while True:
        fila_input = input("Fila (0-9): ")
        columna_input = input("Columna (0-9): ")
        if not (fila_input.isdigit() and columna_input.isdigit()):
            print("Introduce números válidos (0-9).")
            continue
        fila = int(fila_input)
        columna = int(columna_input)
        if not (0 <= fila < 10 and 0 <= columna < 10):
            print("Casilla fuera del tablero.")
            continue
        resultado = disparar((fila, columna), tablero_maquina, barcos_maquina)
        if resultado == "repetido":
            continue
        break

def turno_maquina(tablero_jugador, barcos_jugador, disparos_previos):
    while True:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        if (fila, columna) not in disparos_previos:
            disparos_previos.add((fila, columna))
            resultado = disparar((fila, columna), tablero_jugador, barcos_jugador)
            print(f"La máquina ha disparado a ({fila}, {columna})")
            print("--------------------------")
            break

def jugar():
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()
    esloras = [2, 2, 2, 3, 3, 4]
    barcos_jugador = generar_barcos_aleatorios(tablero_jugador, esloras)
    barcos_maquina = generar_barcos_aleatorios(tablero_maquina, esloras)
    disparos_previos = set()
    while True:
        print("Tu tablero")
        mostrar_tablero(tablero_jugador)
        print("--------------------------")
        print("Tablero máquina")
        mostrar_tablero(tablero_maquina, ocultar_barcos=True)
        print("--------------------------")
        print("Tu turno:")
        turno_jugador(tablero_maquina, barcos_maquina)
        if todos_hundidos(tablero_maquina):
            print("¡Has ganado! ¡Has hundido todos los barcos de tu oponente!")
            break
        print("--------------------------")
        print("Turno de la máquina")
        turno_maquina(tablero_jugador, barcos_jugador, disparos_previos)
        if todos_hundidos(tablero_jugador):
            print("¡Has perdido! ¡Tu oponente ha hundido todos tus barcos!")
            break

