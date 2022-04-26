from WorldClass import World

class App:
    def __init__(self):
            self.m_command= ""
            self.m_mundo = World()
            self.m_isRunning = True

    def run(self):
        print("\nEscribe 'Menu' u 'Opciones' para ver el menú de opciones.")
        while self.m_isRunning:
            print('\n')
            self.m_mundo.printRoom()

            m_command = str.lower(input("Movimiento (w/a/s/d) = "))
            if m_command == "w" or m_command == "a" or m_command == "s" or m_command == "d":
                print("El jugador se movio.")
                self.m_mundo.moveplayer(m_command)

            elif m_command == "menu" or m_command == "opciones":
                print("\n\nUsar puertas:  . . . . . . . (use door/usar puerta/door/puerta)")
                print("Usar llaves y abrir puertas: (open door/abrir puerta/open/abrir)")
                print("Utilizar objetos:  . . . . . (use/usar)")
                print("Usar Mágia:  . . . . . . . . (mana//mágia/magic)")
                print("Tirar/deshechar objetos: . . (throw/trash/tirar/deshechar)")
                print("Soltar objetos : . . . . . . (drop/soltar/colocar)")
                print("Recoger objetos: . . . . . . (pick/pick up/recoger/agarrar)")
                print("Mirar inventario:  . . . . . (inv/inventory/inventario/status/objects/objetos)")
                print("Inspeccionar Enemigo:  . . . (inspect/inspeccionar/investigate/investigar)")
                print("Luchar:  . . . . . . . . . . (fight/combat/luchar/combatir/pelear)")
                print("Salir del juego: . . . . . . (close game/cerrar juego/give up/rendirse)\n")
                print("Un 0 en el mapa significa Espacio Libre.")
                print("Un 1 en el mapa significa Pared.")
                print("Un 2 en el mapa significa Ahujero/Vacío.")
                print("Un 3 en el mapa significa Púas y Pinchos.")
                print("La P en el mapa simboliza al Jugador.\n")
                print("Una D en el mapa simboliza una Puerta.")
                print("Una X en el mapa simboliza un Objeto.")
                print("Una D en el mapa simboliza una Puerta.")
                print("Una E en el mapa simboliza un Enemigo.")

            elif m_command == "use door" or m_command == "usar puerta" or m_command == "door" or m_command == "puerta":
                self.m_mundo.usedoor()

            elif m_command == "open door" or m_command == "abrir puerta" or m_command == "open" or m_command == "abrir":
                self.m_mundo.opendoor()

            elif m_command == "use" or m_command == "usar":
                self.m_mundo.useitem()

            elif m_command == "throw" or m_command == "trash" or m_command == "tirar" or m_command == "deshechar":
                self.m_mundo.throwitem()

            elif m_command == "drop" or m_command == "soltar" or m_command == "colocar":
                self.m_mundo.dropitem()

            elif m_command == "pick" or m_command == "pick up" or m_command == "recoger" or m_command == "agarrar":
                self.m_mundo.pickitem()

            elif m_command == "inv" or m_command == "inventory" or m_command == "status" or m_command == "inventario" or m_command == "objects" or m_command == "objetos":
                self.m_mundo.lookinv()
            
            elif m_command == "fight" or m_command == "combat" or m_command == "luchar" or m_command == "combatir" or m_command == "pelear":
                self.m_mundo.CombatEnemy()

            elif m_command == "maná" or m_command == "mana" or m_command == "magia" or m_command == "mágia"or m_command == "magic":
                self.m_mundo.MagicBoost()

            elif m_command == "inspect" or m_command == "inspeccionar" or m_command == "investigar" or m_command == "investigate":
                self.m_mundo.EnemyInspect()

            elif m_command == "close game" or m_command == "cerrar juego" or m_command == "give up" or m_command == "rendirse":
                self.m_isRunning = False
            else:
                print("\n")

            if self.m_mundo.m_jugador.m_health <=0:
                print("\n")
                print("=====================")
                print("  G A M E   O V E R  ")
                print("    FIN DEL JUEGO    ")
                print("=====================")
                print("\n")
                break