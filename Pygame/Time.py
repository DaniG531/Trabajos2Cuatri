import pygame

class TimeSystem:
    m_current = 0
    m_last = 0
    m_delta = 0

    def GetTime(self): 
        self.m_current = (pygame.time.get_ticks())/1000
        return self.m_current

    def GetDeltaTime(self):
        return self.m_delta
        
    def Update(self):
        self.m_delta = self.m_current - self.m_last 
        self.m_last = (pygame.time.get_ticks())/1000       
        