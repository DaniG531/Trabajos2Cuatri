from ItemClass import Item
from PositionClass import Position

class Mana(Item):
    def __init__(self, pos = Position()):
        super().__init__(pos)
        self.m_restoring = 25