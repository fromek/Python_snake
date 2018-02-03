from Point import Point
from ItemType import ItemType
import pygame
class Item:

    size = 20
    points = 1
    itType = 1
    initTime = 0
    def __init__(self, x,y, iType):
       self._item_surf = None  
       self._location = Point()
       self.reInit(x,y,iType)     
    
    def reInit(self, x, y, iType):
        self.itType = iType
        if ItemType(iType) == ItemType.Apple:
            self.points = 1
            self._item_surf = pygame.image.load("Resources/apple1.png").convert()
        elif ItemType(iType) == ItemType.BigApple:
            self.points = 2
            self._item_surf = pygame.image.load("Resources/bigApple.png").convert()
        elif ItemType(iType) == ItemType.poison:
            self._item_surf = pygame.image.load("Resources/poison.png").convert()
            self.points = 0
        
        self.initTime = pygame.time.get_ticks()
        self._location.x = x *self.size
        self._location.y = y * self.size
        

    def drawItem(self,surface):
        surface.blit(self._item_surf,(self._location.x,self._location.y))

    def getLocation(self):
        return self._location

