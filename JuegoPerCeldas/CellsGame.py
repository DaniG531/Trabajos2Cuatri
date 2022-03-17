import copy
MatrizA = [["0" for i in range(7)] for j in range(8)]
MatrizB = [["0" for i in range(5)] for j in range(5)]
MatrizC = [["0" for i in range(8)] for j in range(4)]
MatrizA[0][6] = "B"
MatrizA[7][1] = "C"
MatrizB[2][4] = "A"
MatrizB[2][3] = "P"
MatrizC[0][1] = "A"
MatrizC[1][1] = "P"

direction = "S"
Matriz = MatrizA
Matriz[3][3] = "P"

def Nope():
    print("")
    print("")
    print("No puedes avanzar más por ahí.")


Pos = [3,3]
NewPos = [3,3]
MatrizInfo = (Matriz, Pos, NewPos)

def Puertas(Matriz, NewPos):
    if Matriz[NewPos[0]][NewPos[1]] == "A":
        Matriz = copy.deepcopy(MatrizA)
        Pos = [3,3]
        destination = [3,3]
        Matriz[3][3] = "P"
        NewInfo = (Matriz, Pos, destination)
        if MatrizA is destination:
            print(True)
        return NewInfo
    if Matriz[NewPos[0]][NewPos[1]] == "B":
        Matriz = copy.deepcopy(MatrizB)
        Pos = [2,3]
        destination = [2,3]
        Matriz[2][3] = "P"
        NewInfo = (Matriz, Pos, destination)
        if NewPos is destination:
            print(True)
        return NewInfo
    if Matriz[NewPos[0]][NewPos[1]] == "C":
        Matriz = copy.deepcopy(MatrizC)
        Pos = [1,1]
        destination = [1,1]
        Matriz[1][1] = "P"
        NewInfo = (Matriz, Pos, destination)
        if NewPos is destination:
            print(True)
        return NewInfo

while True:
    
    print("=======================================")
    print("")
    for i in range(len(Matriz)):
        print(Matriz[i])
    print("") 
    print(f"Opciones de Movimiento: ")
    print(f"  -Arriba    = W, w, 'Arriba', 'Up'.")
    print(f"  -Abajo     = S, s, 'Abajo', Down'.")
    print(f"  -Izquierda = A, a, 'Izquierda', 'Left'.")
    print(f"  -Derecha   = D, d, 'Derecha', 'Right'.")
    print("")
    MenuInput = input(f"Hacia donde quieres moverte?  ")
    print("")
    print("=======================================")
    if MenuInput == "W" or MenuInput == "w" or MenuInput == "Arriba" or MenuInput == "Up":
        if Pos[0] == 0:
            Nope()         #Movimiento Arriba 
        else:
            NewPos[0] -= 1
            if Matriz[NewPos[0]][NewPos[1]] != "0":
                Matriz[Pos[0]][Pos[1]] = "0"
                NewInfo = Puertas(Matriz, NewPos)
                NewPos = NewInfo[2]

                Matriz = NewInfo[0]                
                Pos = NewInfo[1]
                
                Matriz[NewPos[0]][NewPos[1]] = "P"
            Matriz[NewPos[0]][NewPos[1]] = "P"
            Matriz[Pos[0]][Pos[1]] = "0"
            Pos[0] -= 1
    if MenuInput == "S" or MenuInput == "s" or MenuInput == "Abajo" or MenuInput == "Down":
        if Pos[0] == len(Matriz[0]):
            Nope()         #Movimiento Abajo
        else:
            NewPos[0] += 1
            if Matriz[NewPos[0]][NewPos[1]] != "0":
                Matriz[Pos[0]][Pos[1]] = "0"
                NewInfo = Puertas(Matriz, NewPos)
                Matriz = NewInfo[0]
                Pos = NewInfo[1]
                NewPos = NewInfo[2]
                Matriz[NewPos[0]][NewPos[1]] = "P"
            Matriz[NewPos[0]][NewPos[1]] = "P"
            Matriz[Pos[0]][Pos[1]] = "0"
            Pos[0] += 1
    if MenuInput == "A" or MenuInput == "a" or MenuInput == "Izquierda" or MenuInput == "Left":
        if Pos[1] == 0:
            Nope()         #Movimiento Izquierda
        else:
            NewPos[1] -= 1
            if Matriz[NewPos[0]][NewPos[1]] != "0":
                Matriz[Pos[0]][Pos[1]] = "0"
                NewInfo = Puertas(Matriz, NewPos)
                Matriz = NewInfo[0]
                Pos = NewInfo[1]
                NewPos = NewInfo[2]
                Matriz[NewPos[0]][NewPos[1]] = "P"
            Matriz[NewPos[0]][NewPos[1]] = "P"
            Matriz[Pos[0]][Pos[1]] = "0"
            Pos[1] -= 1
    if MenuInput == "D" or MenuInput == "d" or MenuInput == "Derecha" or MenuInput == "Right":
        if Pos[1] == len(Matriz[1])-1:
            Nope()         #Movimiento Derecha
        else:
            NewPos[1] += 1
            if Matriz[NewPos[0]][NewPos[1]] != "0":
                Matriz[Pos[0]][Pos[1]] = "0"
                NewInfo = Puertas(Matriz, NewPos)
                Matriz = NewInfo[0]
                Pos = NewInfo[1] 
                NewPos = NewInfo[2]
                Matriz[NewPos[0]][NewPos[1]] = "P"
            Matriz[NewPos[0]][NewPos[1]] = "P"
            Matriz[Pos[0]][Pos[1]] = "0"
            Pos[1] += 1

    print("")
