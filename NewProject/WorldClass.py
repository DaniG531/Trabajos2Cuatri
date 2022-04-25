from KeyClass import Key
from ManaClass import Mana
from PotionClass import Potion
from RoomClass import Room
from PlayerClass import Player
from DoorClass import Door
from PositionClass import Position
from EnemyClass import Enemy

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
            
            ],

            [

            ]

        ]

        enemies = [
            [
            Enemy("Elfo Debil", Position(5,0,0), 50, 10, {"Key": [],  "Potion": [Potion()], "Mana": [Mana()]}),
            Enemy("Elfo Muy Debil", Position(0,3,0), 30, 5, {"Key": [],  "Potion": [Potion()], "Mana": []}),
            Enemy("Elfo MUY Debil", Position(4,4,0), 10, 2, {"Key": [],  "Potion": [Potion()], "Mana": []}),
            ],

            [
            Enemy("Guardia", Position(1,1,1), 80, 22, {"Key":[Key()],"Potion": [Potion(), Potion(), Potion(), Potion()], "Mana": [Mana(),Mana()]}),
            Enemy("Elfo Fuerte", Position(2,0,1), 50, 15, {"Key": [],  "Potion": [Potion(),Potion()], "Mana": []}),
            Enemy("Elfo Fuerte", Position(3,1,1), 50, 20, {"Key": [],  "Potion": [Potion(),Potion()], "Mana": []})
            ],

            [
            Enemy("El Destructor", Position(5,3,2), 300, 30, {"Key":[Key()],"Potion": [Potion(), Potion(), Potion(), Potion()], "Mana": [Mana(), Mana()]}),
            Enemy("Elfo Guerrero", Position(3,5,0), 120, 23, {"Key": [],  "Potion": [Potion()], "Mana": [Mana(),Mana()]}),
            Enemy("Elfo Guerrero", Position(9,5,0), 85, 15, {"Key": [],  "Potion": [Potion()], "Mana": [Mana()]})
            
            ]

        ]


        for i in range(len(cuartos)):
            self.m_rooms.append(Room(cuartos[i], puertas[i], items[i], enemies[i]))
          
    def moveplayer(self, direction):
        self.m_jugador.Move(self.m_rooms, direction, self.m_rooms[self.m_jugador.m_position.m_room].m_enemies)

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
        
    def MagicBoost(self):
        self.m_jugador.Magic()

    def CombatEnemy(self):
        self.m_jugador.Combat(self.m_rooms[self.m_jugador.m_position.m_room].m_enemies, self.m_rooms[self.m_jugador.m_position.m_room].m_items)

    def EnemyInspect(self):
        self.m_jugador.Inspect(self.m_rooms[self.m_jugador.m_position.m_room].m_enemies)

    def printStuff(self, j, i):
        if self.m_jugador.m_position.m_x == j and self.m_jugador.m_position.m_y == i:
            print("P", end = ", ")
            return

        for enemy in self.m_rooms[self.m_jugador.m_position.m_room].m_enemies:
            if enemy.m_position.m_x == j and enemy.m_position.m_y == i:
                print("E", end = ", ")
                return

        for puerta in self.m_rooms[self.m_jugador.m_position.m_room].m_puertas:
            if puerta.m_position.m_x == j and puerta.m_position.m_y == i:
                print("D", end = ", ")
                return
                             
        for item in self.m_rooms[self.m_jugador.m_position.m_room].m_items:
            if item.m_position.m_x == j and item.m_position.m_y == i:
                print("X", end = ", ")
                return


        else: #el codigo entra si no se entró a los if's de arriba
            print(self.m_rooms[self.m_jugador.m_position.m_room].m_celdas[i][j], end = ", ")

    def printRoom(self):
        for i in range(len(self.m_rooms[self.m_jugador.m_position.m_room].m_celdas)):
            for j in range(len(self.m_rooms[self.m_jugador.m_position.m_room].m_celdas[i])):
                self.printStuff(j, i)    
            print()
