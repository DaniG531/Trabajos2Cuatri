from WorldClass import World

class App:
    def __init__(self):
            self.m_command= ""
            self.m_mundo = World()
            self.m_isRunning = True

    def run(self):
        while self.m_isRunning:
            print('\n\n')
            self.m_mundo.printRoom()

            m_command = str.lower(input("Movimiento (w/a/s/d)= "))
            if m_command == "w" or m_command == "a" or m_command == "s" or m_command == "d":
                print("El jugador se movio.")
                self.m_mundo.moveplayer(m_command)

            elif m_command == "use door":
                self.m_mundo.usedoor()

            elif m_command == "open door":
                self.m_mundo.opendoor()

            elif m_command == "use":
                self.m_mundo.useitem()

            elif m_command == "throw":
                self.m_mundo.throwitem()

            elif m_command == "drop":
                self.m_mundo.dropitem()

            elif m_command == "pick":
                self.m_mundo.pickitem()

            elif m_command == "inv":
                self.m_mundo.lookinv()
            
            elif m_command == "close game":
                self.m_isRunning = False
            else:
                print("\n")

            if self.m_mundo.m_jugador.m_health <=0:
                print("\n")
                print("=====================")
                print("  G A M E   O V E R")
                print("=====================")
                print("\n")
                break