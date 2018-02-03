from Point import Point
from WindowSettings import WindowSettings
from DirectionType import DirectionType
from ItemType import ItemType
class Player:
    location = []
    speed = 20
    direction = DirectionType.Right
    length = 3
    updateCountMax = 1
    updateCount = 0
    windowSettings = 0
    score = 0
    alive = 1
    def __init__(self, length, windSettings):
        self.length = length
        self.direction = DirectionType.Right
        for i in range(0,self.length):
            self.location.append(Point())
            self.location[i].x = i*20
            self.location[i].y =  100

        self.windowSettings = windSettings


    def updatePlayer(self):

        self.updateCount += 1
        if self.updateCount > self.updateCountMax:

            for i in range(self.length-1,0,-1):
                self.location[i].x = self.location[i-1].x           
                self.location[i].y = self.location[i-1].y

            if(DirectionType(self.direction) == DirectionType.Right):
                self.location[0].x += self.speed
            if DirectionType(self.direction) == DirectionType.Left:
                self.location[0].x -= self.speed
            if DirectionType(self.direction) == DirectionType.Up:
                self.location[0].y -= self.speed
            if DirectionType(self.direction) == DirectionType.Down:
                self.location[0].y += self.speed
            
            if  self.location[0].x >= self.windowSettings.width and DirectionType(self.direction) == DirectionType.Right:
                self.location[0].x = 0
            elif self.location[0].x < 0 and DirectionType(self.direction) == DirectionType.Left:
                self.location[0].x = self.windowSettings.width - self.speed

            if  self.location[0].y >= self.windowSettings.height and DirectionType(self.direction) ==  DirectionType.Down:
                self.location[0].y = 20
            elif self.location[0].y < 20 and DirectionType(self.direction) == DirectionType.Up:
                self.location[0].y = self.windowSettings.height - self.speed

            self.updateCount = 0;
    def moveRight(self):
        self.direction = DirectionType.Right

    def moveLeft(self):
        self.direction = DirectionType.Left

    def moveUp(self):
        self.direction = DirectionType.Up

    def moveDown(self):
        self.direction = DirectionType.Down

    def draw(self, surface, image):
        for i in range(0, self.length-1):
            surface.blit(image,(self.location[i].x,self.location[i].y))

    def increases(self, item):
        
        newPartLocation = Point()
        if(DirectionType(self.direction) == DirectionType.Right):
            newPartLocation.x = self.location[self.length-1].x + self.speed
            newPartLocation.y = self.location[self.length-1].y
        if DirectionType(self.direction) == DirectionType.Left:
            newPartLocation.x = self.location[self.length-1].x - self.speed
            newPartLocation.y = self.location[self.length-1].y

        if DirectionType(self.direction) == DirectionType.Up:
            newPartLocation.x = self.location[self.length-1].x
            newPartLocation.y = self.location[self.length-1].y - self.speed

        if DirectionType(self.direction) == DirectionType.Down:
            newPartLocation.x = self.location[self.length-1].x
            newPartLocation.y = self.location[self.length-1].y + self.speed
            
        self.length = self.length + 1
        self.location.append(newPartLocation)
        self.score += item.points

        if ItemType(item.itType) == ItemType.poison:
            self.alive = 0


