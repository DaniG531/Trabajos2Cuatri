class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    def __init__(self):
        self.Position = Position(3, 3)
        self.CurrentRoom = 0
        self.LastPosition = Position(3, 3)

    def Move(self, Rooms, direction):
        
        if direction == "w":
            NewPos = Position(self.Position.x, self.Position.y -1)
            Rooms[self.CurrentRoom].Cells[NewPos.x][NewPos.y]

class Room:
    def __init__(self, x, y):
        self.Cells = [["0" for i in range(x)] for j in range(y)]


class World:
    def __init__(self):
        self.Rooms = [Room(7,8), Room(5,5), Room(8,4)]
        self.Jugador = Player()

    def moveplayer(self, direction):
        self.Jugador.Move(self.Rooms, direction)

Mundo = World()

for i in range(len(Mundo.Rooms[0])):
    for j in range(len(Mundo.Rooms)):
        print(Mundo.Rooms[j][i], end = ", ")
    print()

