from operator import inv
from KeyClass import Key
from ManaClass import Mana
from PotionClass import Potion
from PositionClass import Position

class Enemy:
    def __init__(self, name = "genérico", pos = Position(), health = 50, strength = 15, inv = {"Key": [],  "Potion": [Potion()], "Mana": [Mana()]}):
        self.m_name = name
        self.m_position = pos
        self.m_health = health
        self.m_damageGiven = strength
        
        self.m_inventory = inv

    def emptyInv(self, room):
        if len(self.m_inventory["Mana"]) > 0:
            for mana in self.m_inventory["Mana"]:
                self.m_inventory["Mana"].pop(0)
                room.append(Mana(Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)))
        if len(self.m_inventory["Potion"]) > 0:    
            for potion in self.m_inventory["Potion"]:
                self.m_inventory["Potion"].pop(0)
                room.append(Potion(Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)))
        if len(self.m_inventory["Key"]) > 0:    
            for llave in self.m_inventory["Key"]:
                self.m_inventory["Key"].pop(0)
                room.append(Key(Position(self.m_position.m_x, self.m_position.m_y, self.m_position.m_room)))
            
    