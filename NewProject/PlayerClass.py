from turtle import position
from PositionClass import Position
from RoomClass import Room
from DoorClass import Door
class Player:
    def __init__(self):
        self.m_position = Position(3, 3, 0)
        self.m_health = 100

    def UseDoor(self, doors):
        for door in doors:
            if self.m_position.m_x == door.m_position.m_x and self.m_position.m_y == door.m_position.m_y:
                self.m_position = door.m_destination
                return 
        

    def Move(self, Rooms, direction):
        NewPos = Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)

        if direction == "w":
            NewPos.m_y -= 1
            
        if direction == "a":
            NewPos.m_x -= 1

        if direction == "s":
            NewPos.m_y += 1

        if direction == "d":
            NewPos.m_x += 1

        if Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 1:
            print("U not.", end= "\n\n" )
        elif Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 2:
            print("U ded.", end= "\n\n")
            self.m_health = 0
        elif Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 3:
            print("U hurt.", end= "\n\n")
            self.m_health -= 10
        else:        
            self.m_position = NewPos