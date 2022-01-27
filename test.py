class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalizacion(self):
        i = ((self.x**2)+(self.y**2))**(0.5)
        normX = self.x/i
        normY = self.y/i
        VectorNorm = Vector(normX, normY)
        return VectorNorm

V1 = Vector(float(4), float(3))
V1.normalizacion()

print(V1.normalizacion())