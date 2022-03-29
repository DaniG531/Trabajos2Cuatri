from WorldClass import World

class App:
    def __init__(self):
            self.m_command= ""
            self.m_mundo = World()
            self.m_isRunning = True

    def run(self):
        while self.m_isRunning:
            self.m_mundo.printRoom()

            m_command = str.lower(input("Movimiento (w/a/s/d)= "))
            if m_command == "w" or m_command == "a" or m_command == "s" or m_command == "d":
                print("El jugador se movio.")
                self.m_mundo.moveplayer(m_command)

            elif m_command == "use door":
                self.m_mundo.usedoor()
            