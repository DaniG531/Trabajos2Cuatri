List = []

class Person:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

def datos():
    print("=====================================")
    nombre = input("Escribe el Nombre de la Persona:   ")
    apellido = input("Escribe el Apellido de la Persona:   ")
    edad = input("Escribe la Edad de la Persona:   ")
    genero = input("Escribe el Género de la Persona:   ")
    print("=====================================")
    print("")
    DatosPersona = Person(nombre, apellido, edad, genero)
    return DatosPersona

def AumentarEdad():
    print("=====================================")
    AumentedAge = int(input("Escribe la edad a aumentar:   "))
    print("- - - - - - - - - - - - ")
    IndexNumber = int(input("Escribe cada que número de personas en la lista:   "))
    for i in range(0, int(len(List)), IndexNumber):
        setattr(List[i], "edad", AumentedAge + int(getattr(List[i], "edad")))
    print("=====================================")

def Imprimir():
    Z = 1
    for i in List:
        print("- - - - - - - - - - - - ")
        print(f"Persona #", Z ,": ")
        for ii in vars(i):
            print(ii, ": ", getattr(i,ii))
        print("- - - - - - - - - - - - ")
        Z += 1

def Menu():
    print("")
    print("Elige una opción.")
    print("=====================================")
    print("   1. Agregar una persona a la lista.")
    print("   2. Aumentar edad.")
    print("=====================================")
    menuopcion = int(input())
    if menuopcion == 1:
        A = True
        while A:
            List.append(datos())
            print("¿Agregar a alguien más? ")
            print("   1. Sí.")
            print("   2. No.")
            print("- - - - - - - - - - - - ")
            answer = int(input())
            if answer == 2:
                A = False
    if menuopcion == 2:
        if len(List) <= 1:
             print("- - - - - - - - - - - - ")
             print("No hay valores en la lista.")
             print("- - - - - - - - - - - - ")
        else:
            AumentarEdad()

    if len(List) > 0:
        print("=====================================")
        print("Lista de Personas.")
        Imprimir()


print("[][][][][][][][][][][][][][][][][][][]")
print("[][][][][][][][][][][][][][][][][][][]")
B = True
while B:
    Menu()
    print("¿Volver Al Menú? ")
    print("   1. Sí.")
    print("   2. No.")
    print("- - - - - - - - - - - - ")
    answer = int(input())
    if answer == 2:
        B = False

