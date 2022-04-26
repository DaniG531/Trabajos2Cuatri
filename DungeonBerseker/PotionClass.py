from ItemClass import Item
from PositionClass import Position

class Potion(Item):
    def __init__(self, pos = Position()):
        super().__init__(pos)
        self.m_healing = 25