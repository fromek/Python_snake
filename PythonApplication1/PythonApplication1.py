
from pygame.locals import *
import pygame
from Point import Point
from WindowSettings import WindowSettings
from Player import Player
import time
from Item import Item
from CollisionManager import CollisionManager
from random import randint

class App:

    windowSettings = 0
    player = 0
    item = 0
    collisionMgr = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._item_surf = None       
        self.windowSettings = WindowSettings()
        self.windowSettings.width = 800
        self.windowSettings.height = 600
        self.player = Player(3,self.windowSettings)
        self.item = Item(5,5)
        self.collisionMgr = CollisionManager()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowSettings.width, self.windowSettings.height), pygame.HWSURFACE)

        pygame.display.set_caption('Projekt PPP pygame')
        self.running = True
        self._image_surf = pygame.image.load("snakeImg.png").convert()
        self._item_surf = pygame.image.load("item1Img.png").convert()
        
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.updatePlayer()

        for i in range(0,self.player.length-1):
            if self.collisionMgr.collisionDetected(self.player.location[i],self.item.location,16):
                self.item.location.x = randint(1,self.windowSettings.width/self.item.size-1) * self.item.size
                self.item.location.y = randint(1,self.windowSettings.height/self.item.size-1) * self.item.size
                self.player.increases(self.item.points)
    
        for i in range(2,self.player.length-1):
            if self.collisionMgr.collisionDetected(self.player.location[i],self.player.location[0],16):
                print("Game Over!")
                print("{} {}".format("Your score:", self.player.score))
                self._running = False

        pass


    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.item.draw(self._display_surf, self._item_surf)
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
            
               
    
        
        
