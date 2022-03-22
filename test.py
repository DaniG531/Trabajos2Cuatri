import pygame

def GetTime(): 
    totalTicks = (pygame.time.get_ticks())/1000
    print(str(f"{totalTicks} segundos desde que inició el programa."))

GetTime()