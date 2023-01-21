from solutions.vo import Point

class Line:
    # Constructor method
    # Defining a line of the form y = mx + c
    # slope = Slope of the Line
    # constant = Constant of the Line
    # Slope of None is a line parallel to y-axis (Vertial Lines)
    # Slope of 0 is a line parallel to x-axis (Horizontal Lines)
    def __init__(self, m=None, c=0):
        self.m = m
        self.c = c    

    @classmethod
    def from_XY(cls, X: list[int], Y:list[int]):
        if not X: return cls()
        if not Y: return cls()

        x1, y1 = X
        x2, y2 = Y

        if x1 == x2: m = None; c = x1
        elif y1 == y2: m = 0; c = y1
        else: m = (y2 - y1) / (x2 - x1); c = y1 - m*x1

        return cls(m,c)

    @classmethod
    def from_Points(cls, A:Point, B:Point):
        if not A: return cls()
        if not B: return cls()

        aList = [A.x, A.y]
        bList = [B.x, B.y]

        return cls(aList, bList)


    # String value for printing Line in the form y = mx + c 
    def __str__(self):
        if not self.m:
            return "x = " + str(self.c)
        
        if self.m == 0:
            return "y = " + str(self.c)

        return "y = " + "(" + str(self.m) +")" + "x + (" + str(self.c) + ")"

    def __eq__(self, other):
        if isinstance(other, Line):
            if self.m is None and other.m is None and self.c == other.c: return True
            if self.m == other.m and self.c == other.c: return True

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.m, self.c))

