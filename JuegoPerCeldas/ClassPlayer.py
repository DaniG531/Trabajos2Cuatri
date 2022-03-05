from ClassPosition import *
from ClassRoom import *
from ClassWorld import *

class Player:
    def __init__(self):
        self.Position = Position(3, 3)
        self.CurrentRoom = 0
        self.LastPosition = Position(3, 3)

    def Move(self, Rooms, direction):
        
        if direction == "w":
            NewPos = Position(self.Position.x, self.Position.y -1)
            Rooms[self.CurrentRoom].Cells[NewPos.x][NewPos.y]