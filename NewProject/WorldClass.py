from RoomClass import Room
from PlayerClass import Player

class World:
    def __init__(self):
        self.Rooms = [Room(7,8), Room(5,5), Room(8,4)]
        self.Jugador = Player()

    def moveplayer(self, direction):
        self.Jugador.Move(self.Rooms, direction)