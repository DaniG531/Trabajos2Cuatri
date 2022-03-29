from PositionClass import Position

class Door:
    def __init__(self, lugarpuerta, destino, open = True):
        self.m_position = lugarpuerta
        self.m_destination = destino
        self.m_isOpen = open

