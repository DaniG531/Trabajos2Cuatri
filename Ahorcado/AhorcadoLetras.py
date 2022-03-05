Palabra = "uwu"
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
print("")
print("")

for i in range(len(Palabra)):
    print("_", end= " ") 
    list.append("_")
print("")
print("")
print(list)
contador = 10
while 1:
    print(f"Tienes {contador} intentos.")
    letra = input("Escribe una letra:  ")
    print("")

    for i in range(len(Palabra)):
        if letra == Palabra[i]:
            list[i] = letra

    print("")
    print("")
    print(list)

    if letra in list:
        continue
    else:
        contador -= 1
        
    
    if contador == 0:
        break

print("")
print("=================")
print("G A M E   O V E R")
print("=================")
print("")

