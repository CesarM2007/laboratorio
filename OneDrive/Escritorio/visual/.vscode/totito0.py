def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_victoria(tablero, jugador):
    for fila in tablero:
        if all(simbolo == jugador for simbolo in fila):
            return True

    for columna in range(3):
        if all(tablero[fila][columna] == jugador for fila in range(3)):
            return True

    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def jugar_totito():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0

    while True:
        imprimir_tablero(tablero)
        jugador_actual = jugadores[turno % 2]
        fila = int(input(f"Jugador {jugador_actual}, elige una fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugador_actual}, elige una columna (0, 1, 2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            if verificar_victoria(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡Jugador {jugador_actual} ha ganado!")
                break
            turno += 1
        else:
            print("Esa casilla ya está ocupada. Inténtalo de nuevo.")

        if turno == 9:
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break

if __name__ == "__main__":
    jugar_totito()
