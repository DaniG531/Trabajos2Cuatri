import sys
import pygame

pygame.init()

window = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Prueba de Pygame")

icon = pygame.image.load("Pygame/icon.jpg")
pygame.display.set_icon(icon)

isRunning = True

playerSprite = pygame.image.load("Pygame/strob.gif")
playerPosX = 200
playerPosY = 200
PlayerSpeed = 5

playerSpriteHeight = playerSprite.get_height()
playerSpriteWidth = playerSprite.get_width()

playerSpriteHeight /= 2
playerSpriteWidth /= 2

FPS = 60
dt = pygame.time.get_ticks()

def GetTime(): 
    totalSecs = (pygame.time.get_ticks())/1000
    #print(str(f"{totalSecs} segundos desde que inició el programa."))
    return totalSecs

def GetDeltaTime():
    deltime = (dt - (GetTime()))/1000
    return deltime
    
def Update():
    print(str(f"Tiempo desde el inicio = {GetTime()} segundos. \nTiempo entre cada frame = {GetDeltaTime()} segundos."))



class InputSystem:
    def _init_(self):
        self.W_Pressed = False
        self.A_Pressed = False
        self.S_Pressed = False
        self.D_Pressed = False

    def update(self):
        self.W_Down = False
        self.A_Down = False
        self.S_Down = False
        self.D_Down = False
        self.W_Up = False
        self.A_Up = False
        self.S_Up = False
        self.D_Up = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.A_Pressed = True
                    self.A_Down = True

                if event.key == pygame.K_d:
                    self.D_Pressed = True
                    self.D_Down = True

                if event.key == pygame.K_w:
                    self.W_Pressed = True
                    self.W_Down = True

                if event.key == pygame.K_s:
                    self.S_Pressed = True
                    self.S_Down = True


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.A_Pressed = False
                    self.A_Up = True

                if event.key == pygame.K_d:
                    self.D_Pressed = False
                    self.D_Up = True

                if event.key == pygame.K_w:
                    self.W_Pressed = False
                    self.W_Up = True

                if event.key == pygame.K_s:
                    self.S_Pressed = False
                    self.S_Up = True


    def GetKey(self, key):
        if key == "W":
            return self.W_Pressed
        if key == "A":
            return self.A_Pressed
        if key == "S":
            return self.S_Pressed
        if key == "D":
            return self.D_Pressed

    def GetKeyDown(self, key):
        if key == "W":
            return self.W_Down
        if key == "A":
            return self.A_Down
        if key == "S":
            return self.S_Down
        if key == "D":
            return self.D_Down

    def GetKeyUp(self, key):
        if key == "W":
            return self.W_Up
        if key == "A":
            return self.A_Up
        if key == "S":
            return self.S_Up
        if key == "D":
            return self.D_Up

#        if event.type == pygame.KEYUP:
#            if event.key == pygame.K_a:
#                playerPosX -= PlayerSpeed
#            if event.key == pygame.K_d:
#                playerPosX += PlayerSpeed
#            if event.key == pygame.K_w:
#                playerPosY -= PlayerSpeed
#            if event.key == pygame.K_s:
#                playerPosY += PlayerSpeed



move = InputSystem()



playerSprite = pygame. transform.scale(playerSprite, (playerSpriteWidth, playerSpriteHeight))


while isRunning:
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT: sys.exit()
                #if event.key == pygame.K_b:
                    #GetTime()
     
    
    GetTime()
    Tiempo = GetTime()
    #print(Tiempo )
    print()
    
    TiempoDelta = GetDeltaTime()
    #print(TiempoDelta)
    print()

    Update()

    window.fill((130, 20, 210))
    window.blit(playerSprite, (playerPosX, playerPosY))
    pygame.display.update()