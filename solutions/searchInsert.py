"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104


"""

class Solution:
    def searchInsert(self, nums: list[int], n: int) -> int:

        start = 0
        end = len(nums) - 1

        #while (start <= end and start >= 0 and end < len(nums)):
        while (start <= end):
            x = (start + end) // 2
            if (n == nums[x]):
                return x
            else:
                if n < nums[x]:
                    end = x - 1
                else:
                    start = x + 1
        
        return start


