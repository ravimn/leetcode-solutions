"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        r = []
        hashMap = {nums[i]: i for i in range(0, len(nums))}

        for i in range(0, len(nums)):
            y = target - nums[i]
            if (y in hashMap and y != nums[i]):
                print(nums[i], target - nums[i])
                r.append(i)
                r.append(hashMap.get(target - nums[i]))
                return r
 
        if len(r) == 0:
            x = target / 2
            for i in range(0, len(nums)):
                if nums[i] == x:
                    r.append(i)
                    if (len(r) == 2):
                        return r
        
        #Return empty String
        return r
    def twoSumSortedArray(self, nums:list[int], target:int) -> list[int]:
        result = []
        x = 0; y = len(nums) - 1

        while x < y:
            sum_xy = nums[x] + nums[y]
            if sum_xy == target:
                result.append(x+1)
                result.append(y+1)
                return result
            
            if sum_xy > target:
                y -= 1
            else:
                x += 1
        return result
