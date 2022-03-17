import copy

cuarto1 = [[1,1,1],[1,1,1],[1,1,1]]
cuarto1_tem = copy.deepcopy(cuarto1)
jugador = [1, 1]
tem_jugador = jugador
mov = ''
cuarto1_tem[jugador[0]][jugador[1]] = 'J'

def print_room():
  for i in range(3):
        for j in range(3):
            print(cuarto1_tem[i][j], end=" ")
        print()

print_room()

while 1:

    print('a donde quieres mover el jugador?')
    print('')
    mov = str.lower(input('arriba (w), izquierda (a), abajo (s), derecha (d): '))
    print('')

    if mov == 'w':
        if tem_jugador[0] == 0:
            print('ya te encuentras al final del cuarto')
            print('')
        else:
            print('el jugador avanza hacia arriba')
            print('')
            tem_jugador[0] -= 1 
        if cuarto1[tem_jugador[0]][tem_jugador[1]] != 1:
            print('el jugador no puede moverse al lugar esperado')
        else:
            jugador = tem_jugador
            cuarto1_tem = copy.deepcopy(cuarto1)
            cuarto1_tem[jugador[0]][jugador[1]] = 'J'
    
    if mov == 'a':
        if tem_jugador[1] == 0:
            print('ya te encuentras al final del cuarto')
            print('')
        else:
            print('el jugador avanza hacia la izquierda')
            print('')
            tem_jugador[1] -= 1 
        if cuarto1[tem_jugador[0]][tem_jugador[1]] != 1:
            print('el jugador no puede moverse al lugar esperado')
        else:
            jugador = tem_jugador
            cuarto1_tem = copy.deepcopy(cuarto1)
            cuarto1_tem[jugador[0]][jugador[1]] = 'J'
    
    if mov == 's':
        if tem_jugador[0] == 2:
            print('ya te encuentras al final del cuarto')
            print('')
        else:
            print('el jugador avanza hacia abajo')
            print('')
            tem_jugador[0] += 1 
        if cuarto1[tem_jugador[0]][tem_jugador[1]] != 1:
            print('el jugador no puede moverse al lugar esperado')
        else:
            jugador = tem_jugador
            cuarto1_tem = copy.deepcopy(cuarto1)
            cuarto1_tem[jugador[0]][jugador[1]] = 'J'
        
    if mov == 'd':
        if tem_jugador[1] == 2:
            print('ya te encuentras al final del cuarto')
            print('')
        else:
            print('el jugador avanza hacia la derecha')
            print('')
            tem_jugador[1] += 1 
        if cuarto1[tem_jugador[0]][tem_jugador[1]] != 1:
            print('el jugador no puede moverse al lugar esperado')
        else:
            jugador = tem_jugador
            cuarto1_tem = copy.deepcopy(cuarto1)
            cuarto1_tem[jugador[0]][jugador[1]] = 'J'    
    
    print_room()
