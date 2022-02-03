val = False

x = int(input("Introduce tamaño de la Matriz:  "))
while x % 2 == 0:
    print("El número no es par. Elige otro número.")
    x = int(input("Introduce tamaño de la Matriz:  "))
y = x

matriz = [[False for i in range(x)] for j in range(y)]
print("")
def reset():
    for i in range(len(matriz)):
        print(matriz[i])
print("")
print("")



for i in range(len(matriz)):
    for j in range(i+1):
        matriz[i][j] = True
    for j in range(i):
        matriz[i][j] = False
for i in range(len(matriz)):
    print(matriz[i])
print("")
print("")


for i in range(len(matriz)):
    for j in range(i+1):
        matriz[i][j] = False


for i in range(len(matriz)):
    matriz[i][2] = True
for i in range(len(matriz[2])):
    matriz[2][i] = True
for i in range(len(matriz)):
    print(matriz[i])

