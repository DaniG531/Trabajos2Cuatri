class Room:
    def __init__(self, cuarto, puerta, item):
        self.m_celdas = cuarto
        self.m_puertas = puerta
        self.m_items = item
        #self.m_items = objetos

        #self.m_celdas = [[0 for i in range(x)] for j in range(y)]

        # 0 = Espacio libre
        # 1 = Espacio bloqueado
        # 2 = Hoyo
        # 3 = Puas