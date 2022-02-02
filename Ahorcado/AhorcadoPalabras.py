list = []


print("")
print("     ¡========* ")
print("    //        !") 
print("    ||        O")
print("    ||       -|-")
print(F"    ||       / {chr(92)}")
print("    ||")
print("    ||")
print("_-=====================-_")
print("||                     ||")
print("+===========-===========+")
print(" Selecciona  Dificultad")
print("+===========-===========+")
print("    1. - Facil")
print("    2. - Media")
print("    3. - Dificil")
print("")


dificultad = int(input(" .-"))
while dificultad >=4 or dificultad <=0:
    print("Elige una opción valida.")
    dificultad = int(input(" -"))
    
if dificultad == 1:
    Palabra = "paracaidas"
    contador = 30
    for i in range(len(Palabra)):
        print("_", end= " ") 
        list.append("_")
    list[0] = "*"
    list[3] = "*"
    list[4] = "*"

if dificultad == 2:
    Palabra = "helicoptero"
    contador = 20
    for i in range(len(Palabra)):
        print("_", end= " ") 
        list.append("_")
    list[2] = "*"
    list[5] = "*"

if dificultad == 3:
    Palabra = "supercalifrastilisticoespiralidoso"
    contador = 10
    for i in range(len(Palabra)):
        print("_", end= " ") 
        list.append("_")
    list[0] = "*"


print("")
print("")
print(list)

Juego = True
while Juego:
    print(f"Tienes {contador} intentos.")
    GuessWord = input("Adivina la palabra:  ")
    while len(GuessWord) > len(Palabra):
        print("Tu palabra excede la cantidad de caracteres.")
        contador -= 1
        print(f"Tienes {contador} intentos.")
        GuessWord = input("Adivina la palabra:  ")
    print("")

    for i in range(len(GuessWord)):
        if GuessWord[i] == Palabra[i]:
            list[i] = GuessWord[i]
            

    

    if GuessWord == Palabra:
        print("")
        print("")
        print("=================")
        print("  Y O U   W O N  ")
        print("=================")
        print("")
        break
    if GuessWord == "*":
        for i in range(len(list)):
            if GuessWord == list[i]:
                list[i] = Palabra[i]
    else:
        contador -= 1
    
    print("")
    print("")
    print(list)
    
    if contador == 0:
        print("")
        print("=================")
        print("G A M E   O V E R")
        print("=================")
        print("")
        break



