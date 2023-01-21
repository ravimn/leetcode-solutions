"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""

"""
Define a class Line.
Line is represented by scope and constant
"""
from solutions.vo.Line import Line
from solutions.vo.Point import Point

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        d = {}; maximum = 0
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                l = Line.from_XY(points[i], points[j])
                pointI = Point.from_list(points[i])
                pointJ = Point.from_list(points[j])
                c = 0
                if not d.get(l):
                    new_dict = {pointI: 1, pointJ: 1}
                    d[l] = new_dict
                    c = len(new_dict)
                else:
                    new_dict = d.get(l)
                    new_dict[pointI] = 1
                    new_dict[pointJ] = 1
                    c = len(new_dict)

                maximum = max(maximum, c)
        
        return maximum
