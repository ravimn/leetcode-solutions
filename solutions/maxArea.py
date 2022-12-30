"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        if not height:
            return 0

        if len(height) <= 1:
            return 0
        
        # Introduce 2 pointers (x,y)
        x = 0
        y = len(height) - 1
        area = 0
        while x < y:
            new_area = min(height[x], height[y]) * (y - x)
            area = new_area if new_area > area else area
            if (height[x] > height[y]) :
                #ht(x) > ht(y) - Move y towards x
                y -= 1
            else:
                # ht(x) <= ht(y) - Move x towards y
                x +=  1
        return area
