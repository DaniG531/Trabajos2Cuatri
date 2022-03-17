from PositionClass import Position

class Player:
    def __init__(self):
        self.Position = Position(3, 3)
        self.CurrentRoom = 0
        self.LastPosition = Position(3, 3)

    def Move(self, Rooms, direction):
        if direction == "w":
            NewPos = Position(self.Position.x, self.Position.y -1)
            Rooms[self.CurrentRoom].Celdas[NewPos.x][NewPos.y]
            print(Rooms[self.CurrentRoom].Celdas[NewPos.x][NewPos.y])

        if direction == "a":
            NewPos = Position(self.Position.x -1, self.Position.y)
            Rooms[self.CurrentRoom].Celdas[NewPos.x][NewPos.y]
            print(Rooms[self.CurrentRoom].Celdas[NewPos.x][NewPos.y])

        if direction == "s":
            NewPos = Position(self.Position.x, self.Position.y +1)
            Rooms[self.CurrentRoom].Celdas[NewPos.x][NewPos.y]
            print(Rooms[self.CurrentRoom].Celdas[NewPos.x][NewPos.y])

        if direction == "d":
            NewPos = Position(self.Position.x +1, self.Position.y)
            Rooms[self.CurrentRoom].Celdas[NewPos.x][NewPos.y]
            print(Rooms[self.CurrentRoom].Celdas[NewPos.x][NewPos.y])