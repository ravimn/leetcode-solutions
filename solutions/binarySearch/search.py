"""
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if (target == nums[mid]):
                return mid

            if self._isNumberInLHS(start, mid, end, nums, target):
                end = mid - 1
            else:
                start = mid + 1
        
        return -1
    
    def _isNumberInLHS(self, start:int, mid:int, end:int, nums: List[int], target:int) -> bool:
        if nums[start] <= nums[mid]:
            # If LHS is in ascending order - just find if target is within the start and mid range
            return nums[start] <= target and target <= nums[mid]
        
        isInRHS = nums[mid + 1] <= target and target <= nums[end]
        return not isInRHS
    
if __name__ == '__main__':
    s = Solution()
    ans = s.search([3,1], 1)
    print("The answer is {}".format(ans))

