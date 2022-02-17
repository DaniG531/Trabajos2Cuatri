import random
class Vector: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def suma(vector1, vector2):
        suma_x = vector1.x + vector2.x
        suma_y = vector1.y + vector2.y
        SumaVector = Vector (suma_x, suma_y)
        return SumaVector 
    def resta(vector1, vector2):
        resta_x = vector1.x - vector2.x
        resta_y = vector1.y - vector2.y
        RestaVector = Vector (resta_x, resta_y) 
        return RestaVector
    def multiplicacion(vector1, value):
        mult_x = vector1.x * value
        mult_y = vector1.y * value
        MultVector = Vector (mult_x, mult_y)
        return MultVector
    def normalizacion(vector1):
        z = ((vector1.x**2)+(vector1.y**2))**(0.5)
        n_x = vector1.x/z
        n_y = vector1.y/z
        NormVector = Vector (n_x, n_y)
        return NormVector

v_a = Vector(float(random.randint(0,10)), float(random.randint(0,10)))
v_b = Vector(float(random.randint(0,10)), float(random.randint(0,10)))

valor = random.randint(1, 10)
def menu():
    print("--Elige la opción que más te guste:")
    print("")
    print("-Presiona 1 para sumar")
    print("")
    print("-Presiona 2 para restar")
    print("")
    print("-Presiona 3 para multiplicar")
    print("")
    print("-Presiona 4 para normalizar")
    print("")
    print(f"Vector 1 = {v_a.x},{v_a.y}")
    print(f"Vector 2 = {v_b.x},{v_b.y}")
    print("")
    eleccion = int(input(""))
    print("")
    if eleccion == 1:
        v_c = Vector.suma(v_a, v_b)
        print(f"Suma = {v_c.x},{v_c.y}")
    elif eleccion == 2:
        v_c = Vector.resta(v_a, v_b)
        print(f"Resta = {v_c.x},{v_c.y}")
    elif eleccion == 3:
        v_c = Vector.multiplicacion(v_a, valor)
        v_d = Vector.multiplicacion(v_b, valor)
        print(f"El valor por el que se multiplico fue {valor}")
        print("")
        print(f"Multiplicación 1 = {v_c.x},{v_c.y}")
        print("")
        print(f"Multiplicación 2 = {v_d.x},{v_d.y}")
    elif eleccion == 4:
        v_c = Vector.normalizacion(v_a)
        v_d = Vector.normalizacion(v_b)
        print(f"El valor por el que se normalizó fue {valor}")
        print("")
        print(f"Normalización 1 = {v_c.x},{v_c.y}")
        print("")
        print(f"Normalización 2 = {v_d.x},{v_d.y}")

menu()
