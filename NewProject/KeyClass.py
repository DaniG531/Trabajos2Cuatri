from ItemClass import Item
from PositionClass import Position

class Key(Item):
    def __init__(self, pos = Position()):
        super().__init__(pos)