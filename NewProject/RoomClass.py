class Room:
    def __init__(self, x, y):
        self.Celdas = [["0" for i in range(x)] for j in range(y)]