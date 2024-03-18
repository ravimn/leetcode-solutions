"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

import sys


class Solution:

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        #first order of business - sort the array
        nums.sort()
        l = len(nums)
        closestSum = sys.maxsize
        for i in range( l - 2 ):

            left = i + 1
            right = l - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == target:
                    return currentSum
                
                if abs(target - currentSum) < abs(target - closestSum):
                    closestSum = currentSum

                if currentSum < target:
                    left += 1
                else:
                    right -= 1
        
        return closestSum
                




 



