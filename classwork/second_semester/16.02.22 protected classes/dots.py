class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        if self.x == other.x:
            return self.y > other.y
        elif self.y > other.y:
            return self.x > other.x
        return False

    def __ge__(self, other):
        if self.x == other.x:
            return self.y < other.y
        elif self.y > other.y:
            return self.x < other.x
        return False

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Dot(x,y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Dot(x,y)