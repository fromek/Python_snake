
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
            self.items.append(Item(randint(1,self.windowSettings.width/self.itemSize - 1),randint(1,self.windowSettings.height/self.itemSize  -1), randint(1,3)))

        

        self.collisionMgr = CollisionManager()


        self.running = True
        self._image_surf = pygame.image.load("Resources/snakeImg.png").convert()

        
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.updatePlayer()

        for i in range(0,self.player.length-1):
            for j in range(0,self.itemCount):
                if self.collisionMgr.collisionDetected(self.player.location[i],self.items[j].getLocation(),16):
                    self.player.increases(self.items[j])
                    self.items[j].reInit(randint(1,self.windowSettings.width/self.itemSize ),randint(1,self.windowSettings.height/self.itemSize ),randint(1,3))
                    
    
        for i in range(2,self.player.length-1):
            if self.collisionMgr.collisionDetected(self.player.location[i],self.player.location[0],16):
               self.player.alive = 0
        
        for j in range(0,self.itemCount):
            if  pygame.time.get_ticks() - self.items[j].initTime > 10000:
                self.items[j].reInit(randint(1,self.windowSettings.width/self.itemSize - 1),randint(1,self.windowSettings.height/self.itemSize  -1), randint(1,3))

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
            
               
    
        
        
