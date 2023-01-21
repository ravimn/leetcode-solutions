"""
Class that represents a Point(X,Y) in a 2D Space
"""


class Point:
    """
    Contructor that defines a point by passing the X & Y co-oridinates
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #Constructor method that constructs and instance of the class from an int list
    @classmethod
    def from_list(cls, coordinates: list[int]):
        if not coordinates:
            return cls()
        
        if len(coordinates) < 2:
            return cls()

        return cls(coordinates[0], coordinates[1])

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other): return not self.__eq__(other)

    def __hash__(self): return hash((self.x, self.y))

    def __str__(self): return "X:" + str(self.x) + " Y:" + str(self.y)

    



    
        