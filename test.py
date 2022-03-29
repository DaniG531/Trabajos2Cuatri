if Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 1:
                print("U not.", end= "\n\n" )
            elif Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 2:
                print("U ded.", end= "\n\n")
                self.m_health = 0
            elif Rooms[NewPos.m_room].m_celdas[NewPos.m_y][NewPos.m_x] == 3:
                print("U hurt.", end= "\n\n")
                self.m_health -= 10
            else:        
                self.m_position.y -= 1

            #NewPos = Position(self.m_position.x, self.m_position.y -1)
            #Rooms[self.m_position.m_room].Celdas[NewPos.x][NewPos.y]
            #print(Rooms[self.m_position.m_room].Celdas[NewPos.x][NewPos.y])