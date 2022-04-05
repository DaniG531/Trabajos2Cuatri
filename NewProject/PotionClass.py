from ItemClass import Item

class Potion:
    def __init__(self, pos = ()):
        self.m_position = pos
        super(Item)
        self.m_healing = 25