from Point import Point
from WindowSettings import WindowSettings

class Player:
    location = [Point]
    speed = 20
    direction = 0
    length = 3
    updateCountMax = 1
    updateCount = 0
    windowSettings = 0
    score = 0

    def __init__(self, length, windSettings):
        self.length = length
        for i in range(0,length-1):
            self.location.append(Point())

        #domyślne ustaienie pozycji, brak kolizji
        self.location[1].x = 1*20
        self.location[2].x = 2*20

        self.windowSettings = windSettings


    def updatePlayer(self):

        self.updateCount += 1
        if self.updateCount > self.updateCountMax:
            for i in range(self.length-1,0,-1):
                if self.location[i-1].x >= self.windowSettings.width:
                    self.location[i-1].x = 0
                elif self.location[i-1].x < 0:
                    self.location[i-1].x = self.windowSettings.width

                self.location[i].x = self.location[i-1].x           
                
                if self.location[i-1].y >= self.windowSettings.height:
                    self.location[i-1].y = 0
                elif self.location[i-1].y < 0:
                    self.location[i-1].y = self.windowSettings.height

                self.location[i].y = self.location[i-1].y

            if(self.direction == 0):
                self.location[0].x += self.speed
            if self.direction == 1:
                self.location[0].x -= self.speed
            if self.direction == 2:
                self.location[0].y -= self.speed
            if self.direction == 3:
                self.location[0].y += self.speed
            
            self.updateCount = 0;
    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length-1):
            surface.blit(image,(self.location[i].x,self.location[i].y))

    def increases(self, points):
        
        newPartLocation = Point()
        if(self.direction == 0):
            newPartLocation.x = self.location[self.length-1].x + self.speed
            newPartLocation.y = self.location[self.length-1].y
        if self.direction == 1:
            newPartLocation.x = self.location[self.length-1].x - self.speed
            newPartLocation.y = self.location[self.length-1].y

        if self.direction == 2:
            newPartLocation.x = self.location[self.length-1].x
            newPartLocation.y = self.location[self.length-1].y - self.speed

        if self.direction == 3:
            newPartLocation.x = self.location[self.length-1].x
            newPartLocation.y = self.location[self.length-1].y + self.speed
            
        self.length = self.length + 1
        self.location.append(newPartLocation)
        self.score += points


