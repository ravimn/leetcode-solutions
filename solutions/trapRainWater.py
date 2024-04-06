"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

n == height.length
1 <= n <= 2 * 10 ^ 4
0 <= height[i] <= 10 ^ 5

"""
class Solution:
    def trap(self, height:list[int]) -> int:
        length = len(height)
        if length <= 2:
            return 0
        
        leftmax = [0]*length         
        for i in range(1, length):
            leftmax[i] = max(leftmax[i-1], height[i-1])

        rightmax = [0]*length
        for i in range(length-2, 0, -1):
            rightmax[i] = max(rightmax[i+1], height[i+1])

        trap = 0
        for i in range(1, length-1):
            trap += min(leftmax[i], rightmax[i]) - height[i] if min(leftmax[i], rightmax[i]) - height[i] > 0 else 0

        return trap
    
if __name__ == '__main__':
    s = Solution()
    trap = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(trap)



