from Point import Point
class CollisionManager:
    def collisionDetected(self,p1, p2, baseSize):
        if p1.x >= p2.x and p1.x + baseSize == p2.x + baseSize:
            if p1.y >= p2.y and p1.y <= p2.y +baseSize:
                return True
        return False
