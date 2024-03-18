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

    def findShortestSubArray(self, nums: list[int]) -> int:
        count, first, last = {int:int}, {int:int}, {int:int}

        max_degree = 1
        for index, e in enumerate(nums):
            if not e in first:
                first[e] = index
            last[e] = index
            m = count[e] = count.get(e,0) + 1

            max_degree = max(max_degree, m)

        shortest_lenght = len(nums)
        for item, degree in count.items():
            if degree != max_degree:
                continue

            shortest_lenght = min(shortest_lenght, last[item] - first[item] + 1)
        
        return shortest_lenght


                
