from KeyClass import Key
from ManaClass import Mana
from PotionClass import Potion
from RoomClass import Room
from PlayerClass import Player
from DoorClass import Door
from PositionClass import Position

class World:
    m_rooms = []
    
    def __init__(self):
        self.m_jugador = Player()

        cuartos = [

            [
            [0,0,0,0,0,0,0,0],
            [3,0,0,0,0,0,0,3],
            [3,0,0,2,2,0,0,3],
            [0,0,0,2,2,0,0,0],
            [0,0,0,0,0,0,0,0],
            [3,1,1,0,0,1,1,3],
            [0,0,0,0,0,0,0,0]
            ],

            [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
            ],

            [
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,2,2,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0]
            ]

        ]

        puertas = [
            [
            Door(Position(0,3,0),Position(0,3,1))
            ],

            [
            Door(Position(0,3,1),Position(0,3,0)), 
            Door(Position(3,0,1),Position(6,8,2), open = False)
            ],

            [
            Door(Position(6,8,2),Position(3,0,1))
            ]

        ]

        items = [
            [

            ],

            [
            Key(Position(0,0,1))
            ],

            [

            ]


        ]
        for i in range(len(cuartos)):
            self.m_rooms.append(Room(cuartos[i], puertas[i], items[i]))
        
        

    def moveplayer(self, direction):
        self.m_jugador.Move(self.m_rooms, direction)

    def usedoor(self):
        self.m_jugador.UseDoor(self.m_rooms[self.m_jugador.m_position.m_room].m_puertas)

    def opendoor(self):
        self.m_jugador.OpenDoor(self.m_rooms[self.m_jugador.m_position.m_room].m_puertas)

    def lookinv(self):
        self.m_jugador.LookInv()

    def useitem(self):
        self.m_jugador.UseItem()

    def pickitem(self):
        self.m_jugador.PickItem(self.m_rooms[self.m_jugador.m_position.m_room].m_items)

    def dropitem(self):
        self.m_jugador.Drop(self.m_rooms[self.m_jugador.m_position.m_room].m_items)
        
    def throwitem(self):
        self.m_jugador.Throw()

    

    #def pick(self, ):
        #self.m_jugador.PickItem(self.m_rooms[self.m_jugador.m_position.m_room]self.m_items)

    def printRoom(self):
        for i in range(len(self.m_rooms[self.m_jugador.m_position.m_room].m_celdas)):
            for j in range(len(self.m_rooms[self.m_jugador.m_position.m_room].m_celdas[i])):
                if self.m_jugador.m_position.m_x == j and self.m_jugador.m_position.m_y == i:
                    print("P", end = ", ")
                    continue

                for puerta in self.m_rooms[self.m_jugador.m_position.m_room].m_puertas:
                    if puerta.m_position.m_x == j and puerta.m_position.m_y == i:
                        print("D", end = ", ")
                        break
                
                for item in self.m_rooms[self.m_jugador.m_position.m_room].m_items:
                    if item.m_position.m_x == j and item.m_position.m_y == i:
                        print("X", end = ", ")
                        break

                else: #el codigo entra si no se entró a los if's de arriba
                    print(self.m_rooms[self.m_jugador.m_position.m_room].m_celdas[i][j], end = ", ")
            print()
  