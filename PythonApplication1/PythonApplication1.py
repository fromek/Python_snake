
from pygame.locals import *
import pygame
from Point import Point
from WindowSettings import WindowSettings
from Player import Player
import time
from Item import Item
from CollisionManager import CollisionManager
from random import randint
from ItemType import ItemType
class App:

    windowSettings = 0
    player = 0
    items = []
    collisionMgr = 0
    myfont = 0
    itemSize = 20
    itemCount = 5

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None        

    def on_init(self):
        pygame.init()
        self.windowSettings = WindowSettings()
        self.windowSettings.width = 800
        self.windowSettings.height = 600

        self._display_surf = pygame.display.set_mode((self.windowSettings.width, self.windowSettings.height), pygame.HWSURFACE)
        pygame.display.set_caption('Projekt PPP pygame')
        self.myfont = pygame.font.SysFont("monospace", 15)

        self.player = Player(3,self.windowSettings)
        for i in range(0,self.itemCount):
            self.items.append(Item(randint(1,self.windowSettings.width/self.itemSize - 1),randint(1,self.windowSettings.height/self.itemSize  -1), randint(1,2)))

        

        self.collisionMgr = CollisionManager()


        self.running = True
        self._image_surf = pygame.image.load("Resources/snakeImg.png").convert()

        
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def getNewItemType(self):
        maxVal = 3
        poisonCount = 0
        for i in range(0,self.itemCount):
            if ItemType(self.items[i].itType) == ItemType.poison:
                poisonCount += 1
        
        if poisonCount >= 2:
            maxVal = 2

        return randint(1,maxVal)

    def getNewItemPosition(self):
        newPoint = Point()
        newPoint.x = randint(1,self.windowSettings.width/self.itemSize -1)
        newPoint.y = randint(1,self.windowSettings.height/self.itemSize -1)
        while(self.canCreateItemAtPoint(newPoint) == False):
            newPoint.x = randint(1,self.windowSettings.width/self.itemSize -1)
            newPoint.y = randint(1,self.windowSettings.height/self.itemSize -1)

        return newPoint

    def canCreateItemAtPoint(self, point):
        pointToCheck = Point()
        pointToCheck.x = point.x *20
        pointToCheck.y = point.y *20

        for j in range(0,self.itemCount):
            if self.items[j].getLocation().x == pointToCheck.x and self.items[j].getLocation().y == pointToCheck.y:
                return False


        if self.playerHitItem(pointToCheck):
            return False

        return True


    def playerHitItem(self,point):
        for i in range(0,self.player.length-1):
             if self.collisionMgr.collisionDetected(self.player.location[i],point,16):
                 return True

        return False

    def on_loop(self):
        self.player.updatePlayer()
        for j in range(0,self.itemCount):
            if self.playerHitItem(self.items[j].getLocation()):
                self.player.increases(self.items[j])
                newLocation = self.getNewItemPosition()
                self.items[j].reInit(newLocation.x,newLocation.y,self.getNewItemType())
                    
    
        for i in range(2,self.player.length-1):
            if self.collisionMgr.collisionDetected(self.player.location[i],self.player.location[0],16):
               self.player.alive = 0
        
        for j in range(0,self.itemCount):
            if  pygame.time.get_ticks() - self.items[j].initTime > 10000:
                newLocation = self.getNewItemPosition()
                self.items[j].reInit(newLocation.x,newLocation.y, self.getNewItemType())

        pass

        if self.player.alive == 0:
            print("Game Over!")
            print("{} {}".format("Your score:", self.player.score))
            self._running = False

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        for i in range(0,self.itemCount):
            self.items[i].drawItem(self._display_surf)

        self.label = self.myfont.render("{} {}".format("score:", self.player.score), 1, (255,255,255))
        self._display_surf.blit(self.label, (self.windowSettings.height/2, 0))

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if(keys[K_RIGHT]):
                self.player.moveRight()

            if(keys[K_LEFT]):
                self.player.moveLeft()

            if(keys[K_UP]):
                self.player.moveUp()

            if(keys[K_DOWN]):
                self.player.moveDown()

            if(keys[K_ESCAPE]):
               self._running = False

            self.on_loop()
            self.on_render()
            time.sleep(100.0 / 1000.0)

        self.on_cleanup()


if __name__ == "__main__" :
               theApp = App()
               theApp.on_execute()
            
               
    
        
        
