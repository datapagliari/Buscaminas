### JUEGO DE BUSCAMINAS ###

import random

#Crea un tablero de ANCHO x ALTO con un determinado porcentaje de minas
def crea_board(alto, ancho, porcentaje):
    cantmin = (alto*ancho) * porcentaje // 100 
    nomin = alto*ancho - cantmin
    tiles = []
    for element in range(cantmin):
        tiles.append(True)
    for element in range(nomin):
        tiles.append(False)
    tilesshuf = random.shuffle(tiles)
    rta = []
    for element in range(alto):
        rta2 = []
        for elemento in range(ancho):
            rta2.append(tiles[-1])
            tiles.pop()
        rta.append(rta2)
    return rta

#Crea un tablero en donde cada casilla indica las minas que tiene alrededor (del otro tablero)
def mines_arround(matrix):
    rta = []
    alto = len(matrix)
    ancho = len(matrix[0])
    #creacion del esquema de la matrix respuesta
    for ele1 in range(len(matrix)):
        rta.append([])
        for ele2 in range(len(matrix[0])):
            rta[ele1].append(0)
    #print("esquema:",rta)

    ######################################################################

    #caso para la primer línea
    esq1 = matrix[0][1:2] + matrix[1][0:2]
    count = 0
    for item in esq1:
        if item == True:
            count +=1   
    rta[0][0] = str(count)

    for ele2 in range(1, ancho-1):
        coso = matrix[0][ele2-1:ele2] + matrix[0][ele2+1:ele2+2] + matrix[1][ele2-1:ele2+2] 
        count = 0
        for item in coso:
            if item == True:
                count +=1
        rta[0][ele2] = str(count)

    esq1b = matrix[0][ancho-2:ancho-1] + matrix[1][ancho-2:ancho]
    count = 0
    for item in esq1b:
        if item == True:
            count +=1   
    rta[0][ancho-1] = str(count)

    ######################################################################

    #caso para las líneas del medio
    for ele1 in range(1,len(matrix)-1):
        coso = matrix[ele1][1:2] + matrix[ele1-1][0:2] + matrix[ele1+1][0:2]
        count = 0
        for item in coso:
            if item == True:
                count +=1
        rta[ele1][0] = str(count)

    for ele1 in range(1,len(matrix)-1):
        for ele2 in range(1, ancho-1):
            coso = matrix[ele1][ele2-1:ele2] + matrix[ele1][ele2+1:ele2+2] + matrix[ele1-1][ele2-1:ele2+2] + matrix[ele1+1][ele2-1:ele2+2]
            count = 0
            for item in coso:
                if item == True:
                    count +=1
            rta[ele1][ele2] = str(count)

    for ele1 in range(1,len(matrix)-1):
        coso = matrix[ele1][ancho-2:ancho-1] + matrix[ele1-1][ancho-2:ancho] + matrix[ele1+1][ancho-2:ancho]
        count = 0
        for item in coso:
            if item == True:
                count +=1
        rta[ele1][ancho-1] = str(count)

    ######################################################################
    #caso para la última línea
    esq2 = matrix[alto-1][1:2] + matrix[alto-2][0:2]
    count = 0
    for item in esq2:
        if item == True:
            count +=1   
    rta[alto-1][0] = str(count)

    for ele2 in range(1, ancho-1):
        coso = matrix[alto-1][ele2-1:ele2] + matrix[alto-1][ele2+1:ele2+2] + matrix[alto-2][ele2-1:ele2+2] 
        count = 0
        for item in coso:
            if item == True:
                count +=1
        rta[alto-1][ele2] = str(count)

    esq2b = matrix[alto-1][ancho-2:ancho-1] + matrix[alto-2][ancho-2:ancho]
    count = 0
    for item in esq2b:
        if item == True:
            count +=1   
    rta[alto-1][ancho-1] = str(count)
    return rta

#Crea un tablero, ingresando los números de ALTO y ANCHO
def game_board(alto, ancho):
    rta = []
    for element in range(alto):
        rta2 = []
        for elemento in range(ancho):
            rta2.append(".")

        rta.append(rta2)
    return rta

#Función para imprimir el tablero en un formato entendible
def print_tab(tabb):
    print(*table, sep='\n')

#Función para contar la cantidad de casillas vacías
def cuentapuntos(matrix):
    count = 0
    for k in matrix:
        for j in k:
            if j == '.':
                count += 1
    return count

#Mecanismo del juego
def JUEGO():
    #Seteo de dificultad
    #Según el nivel ingresado se elegirán las variables ALTO, ANCHO y cantiadad de minas (en porcentaje)
    dificultad = 11
    while dificultad < 1 or dificultad > 10:
        dificultad = int(input("seleccionar dificultad de 1 a 10: "))
    if dificultad < 4:
        alto, ancho = 6, 6
        porcentaje = 6 + dificultad * 2
    elif dificultad < 7:
        alto, ancho = 8, 8
        porcentaje = 8 + dificultad * 2
    else:
        alto, ancho = 10, 10
        porcentaje = 10 + dificultad * 2
    #Creación de los tableros a usar
    tablero = crea_board(alto, ancho, porcentaje)
    buscaminas = mines_arround(tablero)
    board = game_board(alto, ancho)
    #Calculo de cantidad de minas para determinar el objetivo a cumplir
    cantmin = (alto*ancho) * porcentaje // 100
    print("Jugarás con", alto, "filas y", ancho, "columnas")
    game = True
    while game == True:
        print(*board, sep='\n')
        print("Quedan", cuentapuntos(board) - cantmin, "casillas por descubrir")
        a = int(input("elegí el número de fila: "))-1
        b = int(input("elegí el número de columna: "))-1
        if a == "no" or b == "no":
            break
        elif a <0 or a>alto or b>alto or b<0:
            print("")
            print("número de fila o columna inválido")
            pass
        elif tablero[a][b] == False:
            board[a][b] = buscaminas[a][b]
            
            puntos = cuentapuntos(board)
            if puntos - cantmin == 0: 
                print("GANASTE!")
            else:
                print("\n¡Bien! Continúa:")
                #print("Quedan", puntos - cantmin, "casillas por descubrir")
        else:
            print("\nBum!")
            for j in range(alto):
                for k in range(ancho):
                    if tablero[j][k] == True:
                        board[j][k] = "X"
            print(*board, sep='\n')
            nuevojuego = input("Ingresa 0 si quieres jugar de nuevo")
            if nuevojuego != "0" and nuevojuego != "O":
                game = False
            else:
                dificultad = int(input("seleccionar dificultad de 1 a 10: "))
                if dificultad < 6:
                    alto, ancho = 8, 8
                    porcentaje = 5 + dificultad * 2
                else:
                    alto, ancho = 10, 10
                    porcentaje = 10 + dificultad * 2
                tablero = crea_board(alto, ancho, porcentaje)
                buscaminas = mines_arround(tablero)
                board = game_board(alto, ancho)
                cantmin = (alto*ancho) * porcentaje // 100
                print("")

#Corre el juego
JUEGO()
