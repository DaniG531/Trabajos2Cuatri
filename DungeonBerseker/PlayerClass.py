from KeyClass import Key
from ManaClass import Mana
from PotionClass import Potion
from PositionClass import Position
import random

class Player:
    def __init__(self):
        self.m_position = Position(2, 2, 0)
        self.m_health = 100
        self.m_magic = 25
        self.m_attackOptions = [1,2,3] #1 = Rock, 2 = Paper, 3 = Scissors
        self.m_damageGiven = 25
        
        self.m_inventory = {"Key": [],  "Potion": [Potion(), Potion()], "Mana": [Mana()]}


    def LookInv(self):
        print("Puntos de Vida = ", self.m_health)
        print("Puntos de Magia = ", self.m_magic)
        print("Ataque = ", self.m_damageGiven)
        print("Llaves = ", str(len(self.m_inventory["Key"])))
        print("Pociones de Vida = ", str(len(self.m_inventory["Potion"])))
        print("Pociones de Maná = ", str(len(self.m_inventory["Mana"])))     

    def UseDoor(self, doors):
        for door in doors:
            if self.m_position.m_x == door.m_position.m_x and self.m_position.m_y == door.m_position.m_y:
                if door.m_isOpen == False:
                    print("Puerta Cerrada.\n")
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
                    print("Has recogido una llave.")
                elif isinstance(item,Potion) == True:
                    self.m_inventory["Potion"].append(item)
                    room.pop(room.index(item))
                    print("Has recogido una poción de vida.")
                elif isinstance(item,Mana) == True:
                    self.m_inventory["Mana"].append(item)
                    room.pop(room.index(item))
                    print("Has recogido una poción de maná.")

    def UseItem(self):
        self.LookInv()
        chosenitem = str.lower(input("¿Qué quieres usar? (Llave/Poción de Vida/Poción de Maná) = "))
        if chosenitem == "potion" or chosenitem == "pocion de vida" or chosenitem == "poción de vida" or chosenitem == "poción" or chosenitem == "pocion" or chosenitem == "vida":
            if len(self.m_inventory["Potion"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_health += self.m_inventory["Potion"][0].m_healing
            self.m_inventory["Potion"].pop(0)
            if self.m_health >= 100:
                self.m_health = 100
            print("Puntos de Vida = ", self.m_health)
            print("Pociones de Vida = ", str(len(self.m_inventory["Potion"])))
        
        if chosenitem == "mana" or chosenitem == "pocion de mana" or chosenitem == "poción de maná" or chosenitem == "maná" or chosenitem == "magia" or chosenitem == "mágia":
            if len(self.m_inventory["Mana"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_health += self.m_inventory["Mana"][0].m_restoring
            self.m_inventory["Mana"].pop(0)
            print("Puntos de Maná = ", self.m_magic)
            print("Pociones de Maná = ", str(len(self.m_inventory["Mana"])))

    def Drop(self, room):
        self.LookInv()
        chosenitem = str.lower(input("¿Qué objeto soltar? (Llave/Poción de Vida/Poción de Maná) = "))
        if chosenitem == "key" or chosenitem == "llave":
            if len(self.m_inventory["Key"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Key"].pop(0)
            room.append(Key(Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)))
            print("Keys = ", str(len(self.m_inventory["Key"])))
        elif chosenitem == "potion" or chosenitem == "pocion de vida" or chosenitem == "poción de vida" or chosenitem == "poción" or chosenitem == "pocion" or chosenitem == "vida":
            if len(self.m_inventory["Potion"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Potion"].pop(0)
            room.append(Potion(Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)))
            print("Pociones de Vida = ", str(len(self.m_inventory["Potion"])))
        elif chosenitem == "mana" or chosenitem == "pocion de mana" or chosenitem == "poción de maná" or chosenitem == "maná" or chosenitem == "magia" or chosenitem == "mágia":
            if len(self.m_inventory["Mana"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Mana"].pop(0)
            room.append(Mana(Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)))
            print("Pociones de Maná = ", str(len(self.m_inventory["Mana"])))

    def Throw(self):
        self.LookInv()
        chosenitem = str.lower(input("Que objeto tirar? (Llave/Poción de Vida/Poción de Maná) = "))
        if chosenitem == "key" or chosenitem == "llave":
            if len(self.m_inventory["Key"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Key"].pop(0)
            print("Keys = ", str(len(self.m_inventory["Key"])))
        elif chosenitem == "potion" or chosenitem == "pocion de vida" or chosenitem == "poción de vida" or chosenitem == "poción" or chosenitem == "pocion" or chosenitem == "vida":
            if len(self.m_inventory["Potion"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Potion"].pop(0)
            print("Pociones de Vida = ", str(len(self.m_inventory["Potion"])))
        elif chosenitem == "mana" or chosenitem == "pocion de mana" or chosenitem == "poción de maná" or chosenitem == "maná" or chosenitem == "magia" or chosenitem == "mágia":
            if len(self.m_inventory["Mana"]) <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_inventory["Mana"].pop(0)
            print("Pociones de Maná = ", str(len(self.m_inventory["Mana"])))

    def Magic(self):
        sure = str.lower(input("¿Quieres gastar 25 puntos de Maná para obtener un boost en fuerza? (Y/N) (S/N)= \n"))
        if sure == "y" or sure == "yes" or sure == "yeah" or sure == "sí" or sure == "si" or sure == "s":
            if self.m_magic <= 0:
                print("No tienes objetos de esa clase.\n")
                return
            self.m_magic -= 25
            print("Puntos de Magia = ", self.m_magic)
            self.m_damageGiven += 6
            print("Ataque = ", self.m_damageGiven, "\n")

    def Combat(self, enemies, room):    #1 = Rock, 2 = Paper, 3 = Scissors
        for enemy in enemies:
            if self.m_position.m_x == enemy.m_position.m_x and self.m_position.m_y == enemy.m_position.m_y:
                
                playerAttack = random.choice(self.m_attackOptions)
                if playerAttack == 1:
                    print("\nAtacaste con Piedra.")
                elif playerAttack == 2:
                    print("\nAtacaste con Papel.")
                elif playerAttack == 3:
                    print("\nAtacaste con Tijeras.")
                enemyAttack = random.choice(self.m_attackOptions)
                if enemyAttack == 1:
                    print(f"El enemigo {enemy.m_name} atacó con Piedra.\n")
                elif enemyAttack == 2:
                    print(f"El enemigo {enemy.m_name} atacó con Papel.\n")
                elif enemyAttack == 3:
                    print(f"El enemigo {enemy.m_name} atacó con Tijeras.\n")

                if playerAttack == enemyAttack:
                    print(f"El enemigo {enemy.m_name} y tú atacaron con el mismo ataque. Quedó en empate.")

                if playerAttack == 1 and enemyAttack == 2 or playerAttack == 2 and enemyAttack == 3 or playerAttack == 3 and enemyAttack == 1:
                    #Piedra contra Papel, Papel contra Tijeras, Tijeras contra Piedra.
                    print(f"¡El enemigo {enemy.m_name} ataco primero!")
                    print(f"¡Sufriste {enemy.m_damageGiven} puntos de daño!.\n")
                    self.m_health -= enemy.m_damageGiven
                    print(f"Vida del Jugador = {self.m_health}")
                    print(f"Vida del Enemigo = {enemy.m_health}")

                if playerAttack == 1 and enemyAttack == 3 or playerAttack == 2 and enemyAttack == 1 or playerAttack == 3 and enemyAttack == 2:
                    #Piedra contra Tijeras, Papel contra Piedra, Tijeras contra Papel.
                    print(f"¡Tú atacaste primero!")
                    print(f"El enemigo {enemy.m_name} sufrió {self.m_damageGiven} puntos de daño.\n")
                    enemy.m_health -= self.m_damageGiven
                    print(f"Vida del Jugador = {self.m_health}")
                    print(f"Vida del Enemigo = {enemy.m_health}")

                    if enemy.m_health <= 0:
                        enemy.emptyInv(room)
                        print(f"El enemigo {enemy.m_name} ha muerto y ha soltado lo que llevaba encima.")
                        for enemy in enemies:
                            if self.m_position.m_x == enemy.m_position.m_x and self.m_position.m_y == enemy.m_position.m_y:
                                enemies.pop(enemies.index(enemy))
                
    def Inspect(self, enemies):
        for enemy in enemies:
            if self.m_position.m_x == enemy.m_position.m_x and self.m_position.m_y == enemy.m_position.m_y:
                print(f"\nNombre del enemigo = {enemy.m_name}.")
                print(f"Vida del enemigo = {enemy.m_health}.")
                print(f"Fuerza del enemigo = {enemy.m_damageGiven}.\n")

    def Move(self, Rooms, direction, enemies):
        NewPos = Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)
        
        if direction == "w" or direction == "arriba" or direction == "up":
            NewPos.m_y -= 1          
            
        elif direction == "a" or direction == "izquierda" or direction == "left":
            NewPos.m_x -= 1

        elif direction == "s" or direction == "abajo" or direction == "down":
            NewPos.m_y += 1

        elif direction == "d" or direction == "derecha" or direction == "right":
            NewPos.m_x += 1

        for enemy in enemies:
            if self.m_position.m_x == enemy.m_position.m_x and self.m_position.m_y == enemy.m_position.m_y:
                print("¡No puedes escapar de un combate!")
                return
            

        if NewPos.m_y < 0 or NewPos.m_y >= len(Rooms[self.m_position.m_room].m_celdas):
            print("No puedes moverte por ahí.", end= "\n\n" )
            return

        if NewPos.m_x < 0 or NewPos.m_x >= len(Rooms[self.m_position.m_room].m_celdas[NewPos.m_y]):
            print("No puedes moverte por ahí.", end= "\n\n" )
            return

        if Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 1:
            print("No puedes moverte por ahí.", end= "\n\n" )

        elif Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 2:
            sure = str.lower(input("¿Estás segur@ de quererte mover por ahí? (Y/N) (S/N)= \n"))
            if sure == "y" or sure == "yes" or sure == "yeah" or sure == "sí" or sure == "si" or sure == "s":
                self.m_health = 0
                print(f"\nHas Muerto.\nPuntos de Vida = {self.m_health}", end= "\n\n")
            else:
                return
            

        elif Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 3:
            self.m_health -= 10
            print(f"Te has hecho daño.\nPuntos de Vida = {self.m_health}", end= "\n")
            self.m_position = NewPos

        else:        
            self.m_position = NewPos
            print("\n")

        