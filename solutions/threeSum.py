import itertools
from .twoSum import Solution as twoSum
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        finalList = []
        for i in range(0, len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        l = [nums[i], nums[j], nums[k]]
                        l.sort()
                        print("New list is ", l)
                        finalList.append(l)

        finalList.sort()
        return list(finalList for finalList, _ in itertools.groupby(finalList))
    
    def threeSumUsingTwoSum(self, nums:list[int]) -> list[list[int]]:
        ts = twoSum(); finalist = []
        for x in range(len(nums)):
            n = nums[x]
            copy_array = nums.copy()
            copy_array.pop(x)
            twoSumIndexArray:list[int] = ts.twoSum(copy_array, -n)
            print("n is ", n)
            print("copy_array is ", str(copy_array))
            print("twoSumIndexArray is [" + str(twoSumIndexArray) + " ]" )

            if len(twoSumIndexArray) != 2:
                continue

            newlist = [ n, copy_array[twoSumIndexArray[0]], copy_array[twoSumIndexArray[1]] ]
            newlist.sort()
            finalist.append(newlist)
        
        finalist.sort()
        return list(finalist for finalist, _ in itertools.groupby(finalist))

    def threeSumWithTwoSumTwoPointer(self, nums:list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for index, n in enumerate(nums):
            x = index + 1
            y = len(nums) - 1
            while x < y:                
                sum_nxy = n + nums[x] + nums[y]
                if sum_nxy < 0:
                    x += 1
                    while nums[x] == nums[x-1]:
                        x += 1
                elif sum_nxy > 0:
                    y -= 1
                else:
                    result.append([n, nums[x], nums[y]])
                    break
        return result
            


s = Solution()
print(s.threeSumUsingTwoSum([-1, 0, 1, 2, -1, -4]))