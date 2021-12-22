import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point2):
        dx = self.x - point2.x
        dy = self.y - point2.y
        return math.sqrt(dx * dx + dy * dy)

    def __str__(self):
        return "({}, {})".format(str(self.x), str(self.y))


p1 = Point(4, 9)
p2 = Point(3, 5)
print(p1.distance(p2))
