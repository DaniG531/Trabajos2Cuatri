from WorldClass import World

class App:
    def __init__(self):
            self.m_command= ""
            
    def run(self):
        
        Mundo = World()

        #print(type(Mundo))
        #print(type(Mundo.Rooms[0].Celdas))

        
        while True:
            for i in range(len(Mundo.Rooms[0].Celdas[0])):
                for j in range(len(Mundo.Rooms[0].Celdas[0])):
                    #print(Mundo.Rooms[0].Celdas[j][i], end = ", ")
                    if Mundo.Jugador.Position.x == i and Mundo.Jugador.Position.y == j:
                        print("P", end = ", ")
                    else:
                        print(Mundo.Rooms[0].Celdas[j][i], end = ", ")
                print()
            print(Mundo.Jugador.Position.x, Mundo.Jugador.Position.y)

            
            m_command = str.lower(input("Movimiento (w/a/s/d)= "))
            if m_command == "w" or m_command == "a" or m_command == "s" or m_command == "d":
                print("El jugador se movio arriba")
                Mundo.moveplayer(self.m_command)
            