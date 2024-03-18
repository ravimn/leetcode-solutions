"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

class Solution:

    def findDegree(self, nums:list[int]) -> int:
        m = {int:int}
        degree = 1
        for x in range(len(nums)):
            n = nums[x]
            nCnt = 1
            if n in m:
                nCnt = m[n]
                nCnt = nCnt + 1
                if degree < nCnt:
                    degree = nCnt
            m[n] = nCnt
        return degree

    def findShortestSubArray(self, nums: list[int]) -> int:
        degree = self.findDegree(nums)
        print ("degree of " + str(nums) + " is " + str(degree))
        if degree == 1 or degree == len(nums):
            return degree
        
        for sub_size in range(degree, len(nums)):
            for index in range(len(nums) - sub_size + 1):
                sub_set = nums[index:index+sub_size]
                print ("sub_size [" + str(sub_size) + "] index [" + str(index) + "] sub_set [" + str(sub_set) + "]")
                if degree == self.findDegree(sub_set):
                    print ("Degree matches - returning")
                    return sub_size
        
        print ("Did not find degree - Most likely shortest is the full set")        
        return len(nums)