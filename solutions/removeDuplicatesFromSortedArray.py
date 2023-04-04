"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements 
in the order they were present in nums initially. The remaining elements of nums are not 
important as well as the size of nums.

Return k.

"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        
        k = 1
        i = 1
        n1 = nums[0]
        while i < len(nums):
            n2 = nums[i]
            if n1 != n2:
                nums[k] = n2
                n1 = n2
                k = k + 1

            i = i + 1
        
        return k
