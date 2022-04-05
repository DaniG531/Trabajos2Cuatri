from KeyClass import Key
from ManaClass import Mana
from PotionClass import Potion
from PositionClass import Position


class Player:
    def __init__(self):
        self.m_position = Position(2, 2, 0)
        self.m_health = 100
        self.m_magic = 50
        self.m_lowDamageTaken = 15
        self.m_midDamageTaken = 20
        self.m_hiDamageTaken = 25
        self.m_vHiDamageTaken = 35
        self.m_damageGiven = 10
        self.m_inventory = {"Key": [],  "Potion": [Potion(), Potion()], "Mana": [Mana()]}

    def LookInv(self):
        print("Health = ", self.m_health)
        print("Magic = ", self.m_magic)
        print("Keys = ", str(len(self.m_inventory["Key"])))
        print("Life Potions = ", str(len(self.m_inventory["Potion"])))
        print("Mana Potions = ", str(len(self.m_inventory["Mana"])))
        

    def UseDoor(self, doors):
        for door in doors:
            if self.m_position.m_x == door.m_position.m_x and self.m_position.m_y == door.m_position.m_y:
                if door.m_isOpen == False:
                    print("Closed.\n")
                    return
                self.m_position = door.m_destination
                return 

    def OpenDoor(self, doors):
        for door in doors:
            if self.m_position.m_x == door.m_position.m_x and self.m_position.m_y == door.m_position.m_y:
                if door.m_isOpen == False:
                    self.m_inventory["Key"].pop(0)
                    door.m_isOpen = True
                    print("Se abrió la puerta pero la llave se rompió.\n")

    def PickItem(self, room):
        for item in room:
            if self.m_position.m_x == item.m_position.m_x and self.m_position.m_y == item.m_position.m_y:
                if isinstance(item,Key) == True:
                    self.m_inventory["Key"].append(item)
                    room.pop(room.index(item))
                elif isinstance(item,Potion) == True:
                    self.m_inventory["Potion"].append(item)
                    room.pop(room.index(item))
                elif isinstance(item,Mana) == True:
                    self.m_inventory["Mana"].append(item)
                    room.pop(room.index(item))

    def UseItem(self):
        self.LookInv()
        chosenitem = str.lower(input("Que quieres usar? (Potion/Mana) = "))
        if chosenitem == "potion":
            if len(self.m_inventory["Potion"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_health += self.m_inventory["Potion"][0].m_healing
            self.m_inventory["Potion"].pop(0)
            if self.m_health >= 100:
                self.m_health = 100
            print("Health = ", self.m_health)
            print("Life Potions = ", str(len(self.m_inventory["Potion"])))
        

        if chosenitem == "mana":
            if len(self.m_inventory["Mana"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_health += self.m_inventory["Mana"][0].m_restoring
            self.m_inventory["Mana"].pop(0)
            if self.m_health >= 50:
                self.m_health = 50
            print("Magic = ", self.m_magic)
            print("Mana Potions = ", str(len(self.m_inventory["Mana"])))


    def Drop(self, room):
        self.LookInv()
        chosenitem = str.lower(input("Que objeto soltar? (Key/Potion/Mana) = "))
        if chosenitem == "key":
            if len(self.m_inventory["Key"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Key"].pop(0)
            room.append(Key(Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)))
            print("Keys = ", str(len(self.m_inventory["Key"])))
        elif chosenitem == "potion":
            if len(self.m_inventory["Potion"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Potion"].pop(0)
            room.append(Potion(Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)))
            print("Life Potions = ", str(len(self.m_inventory["Potion"])))
        elif chosenitem == "mana":
            if len(self.m_inventory["Mana"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Mana"].pop(0)
            room.append(Mana(Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)))
            print("Mana Potions = ", str(len(self.m_inventory["Mana"])))


    def Throw(self):
        self.LookInv()
        chosenitem = str.lower(input("Que objeto tirar? (Key/Potion/Mana) = "))
        if chosenitem == "key":
            if len(self.m_inventory["Key"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Key"].pop(0)
            print("Keys = ", str(len(self.m_inventory["Key"])))
        elif chosenitem == "potion":
            if len(self.m_inventory["Potion"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Potion"].pop(0)
            print("Life Potions = ", str(len(self.m_inventory["Potion"])))
        elif chosenitem == "mana":
            if len(self.m_inventory["Mana"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Mana"].pop(0)
            print("Mana Potions = ", str(len(self.m_inventory["Mana"])))
        

    def Move(self, Rooms, direction):
        NewPos = Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)
        
        if direction == "w":
            NewPos.m_y -= 1          
            
        elif direction == "a":
            NewPos.m_x -= 1

        elif direction == "s":
            NewPos.m_y += 1

        elif direction == "d":
            NewPos.m_x += 1

        if NewPos.m_y < 0 or NewPos.m_y >= len(Rooms[self.m_position.m_room].m_celdas):
            print("U not.", end= "\n\n" )
            return

        if NewPos.m_x < 0 or NewPos.m_x >= len(Rooms[self.m_position.m_room].m_celdas[NewPos.m_y]):
            print("U not.", end= "\n\n" )
            return

        if Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 1:
            print("U not.", end= "\n\n" )

        elif Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 2:
            sure = str.lower(input("u sure? (Y/N)= \n"))
            if sure == "y" or sure == "yes":
                self.m_health = 0
                print(f"\nU ded.\nHealth = {self.m_health}", end= "\n\n")
            else:
                return
            

        elif Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 3:
            self.m_health -= 10
            print(f"U hurt.\nHealth = {self.m_health}", end= "\n")
            self.m_position = NewPos

        else:        
            self.m_position = NewPos
            print("\n")

        