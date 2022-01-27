class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, Vect):
        sumaX = self.x + Vect.x
        sumaY = self.y + Vect.y
        VectorSuma = Vector(sumaX, sumaY)
        return VectorSuma

    def __sub__(self, Vect):
        sumaX = self.x - Vect.x
        sumaY = self.y - Vect.y
        VectorResta = Vector(sumaX, sumaY)
        return VectorResta

    def normalizacion(self):
        i = ((self.x**2)+(self.y**2))**(0.5)
        normX = self.x/i
        normY = self.y/i
        VectorNorm = Vector(normX, normY)
        return VectorNorm

    def __mul__(self, valor):
        multiplicacionX = self.x * valor
        multiplicacionY = self.y * valor
        VectorMulti = Vector(multiplicacionX, multiplicacionY)
        return VectorMulti


V1 = Vector(float(input("Valor X del Vector A:  ")), float(input("Valor Y del Vector A:  ")))
print("")
V2 = Vector(float(input("Valor X del Vector B:  ")), float(input("Valor Y del Vector B:  ")))
print("")

def Menu(V1, V2):
    print("")
    print("Elige una opción.")
    print("=====================================")
    print("   1. Definir Vector A.")
    print("   2. Definir Vector B.")
    print("   3. Sumar Vectores.")
    print("   4. Restar Vectores.")
    print("   5. Normalizar Vectores.")
    print("   6. Escalar Vector A.")
    print("   7. Escalar Vector B.")
    print("=====================================")
    print(f"Vector A = {V1.x}, {V1.y}")
    print(f"Vector B = {V2.x}, {V2.y}")
    print("=====================================")

    menuopcion = int(input())
    if menuopcion == 1:
        V1 = Vector(float(input("   Valor X del Vector A = ")), float(input("   Valor Y del Vector A = ")))
        return V1
        
    if menuopcion == 2:
        V2 = Vector(float(input("   Valor X del Vector B = ")), float(input("   Valor Y del Vector B = ")))
        return V2
    if menuopcion == 3:
        V3 = V1.__add__(V2)
        print(f"Suma de Vector A y Vector B = {V3.x}, {V3.y}")
        return V3
    if menuopcion == 4:
        V3 = V1.__sub__(V2)
        print(f"Resta de Vector A y Vector B = {V3.x}, {V3.y}")
        return V3
    if menuopcion == 5:
        V3 = V1.normalizacion()
        V4 = V2.normalizacion()
        print(f"Vector A Normalizado = {V3.x}, {V3.y}")
        print(f"Vector B Normalizado = {V4.x}, {V4.y}")
    if menuopcion == 6:
        V3 = V1.__mul__(float(input("Escribe el valor por el cual quieres escalar:  ")))
        print(f"Vector A escalado = {V3.x}, {V3.y}")
        return V3
    if menuopcion == 7:
        V3 = V2.__mul__(float(input("Escribe el valor por el cual quieres escalar:  ")))
        print(f"Vector B escalado = {V3.x}, {V3.y}")
        return V3
    
    
A = True
while A == True:
    print("=====================================")
    Menu(V1, V2)
    V1 = V1
    V2 = V2


