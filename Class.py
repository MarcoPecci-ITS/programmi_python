class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def classname():
        print("Coordinate")

    # metodo to_string: restituisce self in versione stringa
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

p1 = Coordinate(0,0)
p2 = Coordinate(42,42)

print(p1.getX(), p1.getY())
print(p2.getX(), p2.getY())

Coordinate.classname()

print(Coordinate.__str__(p2))