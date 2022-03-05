#class Sala: 
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#        self.matriz = [[0 for i in range(self.x)] for j in range(self.y)]


MatrizA = [["0" for i in range(7)] for j in range(8)]
MatrizB = [["0" for i in range(5)] for j in range(5)]
MatrizC = [["0" for i in range(8)] for j in range(4)]
MatrizA[0][6] = "B"
MatrizA[7][1] = "C"
MatrizB[2][4] = "A"
MatrizC[0][1] = "A"

direction = "S"
Matriz = MatrizA
Matriz[3][3] = "P"

def Nope():
    print("")
    print("")
    print("No puedes avanzar más por ahí.")

#Sala1 = Sala(7, 8)
#Sala1.CrearSala()
Pos = [3,3]
NewPos = [3,3]
MatrizInfo = [Matriz, Pos, NewPos]

def Puertas(MatrizInfo):
    if MatrizInfo[0][MatrizInfo[2][0]][MatrizInfo[2][1]] == "A":
        MatrizInfo[0] = MatrizA
        MatrizInfo[1] = [3,3]
        MatrizInfo[2] = [3,3]
        MatrizInfo[0][3][3] = "P"
        return MatrizInfo
    if MatrizInfo[0][MatrizInfo[2][0]][MatrizInfo[2][1]] == "B":
        MatrizInfo[0] = MatrizB
        MatrizInfo[1] = [2,3]
        NewPos = [2,3]
        MatrizInfo[0][2][3] = "P"
        return MatrizInfo
    if MatrizInfo[0][MatrizInfo[2][0]][MatrizInfo[2][1]] == "C":
        MatrizInfo[0] = MatrizC
        MatrizInfo[1] = [1,1]
        MatrizInfo[2] = [1,1]
        MatrizInfo[0][1][1] = "P"
        return MatrizInfo

while True:
    
    print("=======================================")
    print("")
    for i in range(len(MatrizInfo[0])):
        print(MatrizInfo[0][i])
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
        if MatrizInfo[1][0] == 0:
            Nope()         #Movimiento Arriba 
        else:
            MatrizInfo[2][0] -= 1
            Puertas(MatrizInfo)
            MatrizInfo[0][MatrizInfo[2[0]]][MatrizInfo[2[1]]] = "P"
            MatrizInfo[0][MatrizInfo[1[0]]][MatrizInfo[1[1]]] = "0"
            MatrizInfo[1][0] -= 1
    if MenuInput == "S" or MenuInput == "s" or MenuInput == "Abajo" or MenuInput == "Down":
        if MatrizInfo[1][0] == len(MatrizInfo[0][0]):
            Nope()         #Movimiento Abajo
        else:
            MatrizInfo[2][0] += 1
            Puertas(MatrizInfo)
            MatrizInfo[0][MatrizInfo[2[0]]][MatrizInfo[2[1]]] = "P"
            MatrizInfo[0][MatrizInfo[1[0]]][MatrizInfo[1[1]]] = "0"
            MatrizInfo[1][0] += 1
    if MenuInput == "A" or MenuInput == "a" or MenuInput == "Izquierda" or MenuInput == "Left":
        if MatrizInfo[1][1] == 0:
            Nope()         #Movimiento Izquierda
        else:
            MatrizInfo[2][1] -= 1
            Puertas(MatrizInfo)
            MatrizInfo[0][MatrizInfo[2[0]]][MatrizInfo[2[1]]] = "P"
            MatrizInfo[0][MatrizInfo[1[0]]][MatrizInfo[1[1]]]= "0"
            MatrizInfo[1][1] -= 1
    if MenuInput == "D" or MenuInput == "d" or MenuInput == "Derecha" or MenuInput == "Right":
        if MatrizInfo[1][1] == len(MatrizInfo[0][1])-1:
            Nope()         #Movimiento Derecha
        else:
            MatrizInfo[2][1] += 1
            Puertas(MatrizInfo)
            MatrizInfo[0][MatrizInfo[2[0]]][MatrizInfo[2[1]]] = "P"
            MatrizInfo[0][MatrizInfo[1[0]]][MatrizInfo[1[1]]] = "0"
            MatrizInfo[1][1] += 1

    
    print("")
