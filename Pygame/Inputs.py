import pygame
import sys
class InputSystem:
    def __init__(self):
        self.W_Pressed = False
        self.A_Pressed = False
        self.S_Pressed = False
        self.D_Pressed = False
        #self.Shf_Pressed = False

    def Update(self):
        self.W_Down = False
        self.A_Down = False
        self.S_Down = False
        self.D_Down = False
        #self.Shf_Down = False

        self.W_Up = False
        self.A_Up = False
        self.S_Up = False
        self.D_Up = False
        #self.Shf_Up = False

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

                #if event.key == pygame.K_LSHIFT:
                #    self.Shf_Pressed = True
                #    self.Shf_Down = True

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

                #if event.key == pygame.K_LSHIFT:
                #    self.Shf_Pressed = True
                #    self.Shf_Up = True

    def GetKey(self, key):
        if key == "W":
            return self.W_Pressed
        if key == "A":
            return self.A_Pressed
        if key == "S":
            return self.S_Pressed
        if key == "D":
            return self.D_Pressed
        #if key == "Shift":
        #    return self.Shf_Pressed

    def GetKeyDown(self, key):
        if key == "W":
            return self.W_Down
        if key == "A":
            return self.A_Down
        if key == "S":
            return self.S_Down
        if key == "D":
            return self.D_Down
        #if key == "Shift":
        #    return self.Shf_Down

    def GetKeyUp(self, key):
        if key == "W":
            return self.W_Up
        if key == "A":
            return self.A_Up
        if key == "S":
            return self.S_Up
        if key == "D":
            return self.D_Up
        #if key == "Shift":
        #    return self.Shf_Up