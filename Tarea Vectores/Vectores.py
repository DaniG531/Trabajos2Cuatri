import pygame, sys, random
pygame.init()

size = width, height = 1000, 1000
center = 500, 500
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)

def colorrandom():
    R = random.randint(5,255)
    G = random.randint(5,255)
    B = random.randint(5,255)
    return [R, G, B]

def plano():
    pygame.draw.line(screen, white, (0, 500), (1000, 500), 1)
    x = 0
    while x <= 1000:
        pygame.draw.rect(screen, white, [x, 490, 1, 20])
        x += 50
    pygame.draw.line(screen, white, (500, 0), (500, 1000), 1)
    x = 0
    while x <= 1000:
        pygame.draw.rect(screen, white, [490, x, 20, 1])
        x += 50

def RandCoords():
    X1 = random.randint(250, 750)
    Y1 = random.randint(250, 750)
    Coords = (X1, Y1)
    return Coords
Coords = RandCoords()


def RandVector():
    VectA = pygame.draw.line(screen, colorrandom(), center, Coords, 5)
    PointA = pygame.draw.circle(screen, colorrandom(), Coords, 5)
    Vect = [VectA, PointA]
    return Vect

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                screen.fill(black)
            if event.key == pygame.K_a:
                
                Coords = RandCoords()
                CoordsA = Coords
                VectorA = RandVector()
                Coords = RandCoords()
                CoordsB = Coords
                VectorB = RandVector()
            if event.key == pygame.K_j:
                #Suma
                CoordsC = (CoordsA[0]+Coords[0]-500), ((CoordsA[1])+Coords[1]-500),
                VectorC = pygame.draw.line(screen, colorrandom(), Coords, CoordsC, 5)
                #VectorCopia
                VectorD = pygame.draw.line(screen, colorrandom(), center, CoordsC, 5)
                PointA = pygame.draw.circle(screen, colorrandom(), CoordsC, 5)
            if event.key == pygame.K_h:
                #Resta
                CoordsC = (CoordsA[0]-Coords[0])+500, ((CoordsA[1])-Coords[1]+500),
                VectorC = pygame.draw.line(screen, colorrandom(), Coords, CoordsC, 5)
                #VectorCopia
                VectorD = pygame.draw.line(screen, colorrandom(), center, CoordsC, 5)
                PointA = pygame.draw.circle(screen, colorrandom(), CoordsC, 5)

    plano()
    
    
    pygame.display.flip()
    pygame.display.update()
    #screen.fill(black)