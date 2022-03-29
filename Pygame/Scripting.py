import pygame
#import random
from Time import TimeSystem
from Inputs import InputSystem

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Prueba de Pygame")

icon = pygame.image.load("Pygame/icon.jpg")
pygame.display.set_icon(icon)

newfont = pygame.font.SysFont("Arial", 30)

isRunning = True

playerSprite = pygame.image.load("Pygame/strob.gif")
playerPosX = 200
playerPosY = 200
PlayerSpeed = 500

playerSpriteHeight = playerSprite.get_height()
playerSpriteWidth = playerSprite.get_width()

playerSpriteHeight /= 2
playerSpriteWidth /= 2

#FPS = 60
dt = pygame.time.get_ticks()


TimeSys = TimeSystem()
Inputss = InputSystem()

#        if event.type == pygame.KEYUP:
#            if event.key == pygame.K_a:
#                playerPosX -= PlayerSpeed
#            if event.key == pygame.K_d:
#                playerPosX += PlayerSpeed
#            if event.key == pygame.K_w:
#                playerPosY -= PlayerSpeed
#            if event.key == pygame.K_s:
#                playerPosY += PlayerSpeed

playerSprite = pygame. transform.scale(playerSprite, (playerSpriteWidth, playerSpriteHeight))

CurrentTime = 0
Delta = 0

while isRunning:
    TimeSys.Update()
    Inputss.Update()
    
    #if Inputss.GetKey("Shift") == True:
    #    PlayerSpeed /= 2
    if Inputss.GetKey("W") == True:
        playerPosY -= PlayerSpeed * Delta
    if Inputss.GetKey("A") == True:
        playerPosX -= PlayerSpeed * Delta
    if Inputss.GetKey("S") == True:
        playerPosY += PlayerSpeed * Delta
    if Inputss.GetKey("D") == True:
        playerPosX += PlayerSpeed * Delta

    print()

    colorr = (0,0,0)#(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    TextTime = newfont.render(f"Time = {CurrentTime} seconds.", False, colorr)
    TextDelta = newfont.render(f"DeltaTime = {Delta} seconds.", False, colorr)

    window.fill((130, 20, 210))
    window.blit(TextTime, (0, 660))
    window.blit(TextDelta, (0, 690))
    window.blit(playerSprite, (playerPosX, playerPosY))
    pygame.display.update()
    
    CurrentTime= TimeSys.GetTime()
    Delta = TimeSys.GetDeltaTime()