from Point import Point
class Item:
    location = Point()
    size = 20
    points = 1

    def __init__(self, x,y):
        self.location.x = x *self.size
        self.location.y = y * self.size

    def draw(self,surface, image):
        surface.blit(image,(self.location.x,self.location.y))

