"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the log level to DEBUG to capture all types of log messages
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Specify the log message format
    handlers=[
#        logging.FileHandler('app.log'),  # Log messages to a file named 'app.log'
        logging.StreamHandler()  # Also log messages to the console
    ]
)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_index = 0
        max_index = len(nums) - 1

        while min_index <= max_index:
            if nums[min_index] > nums[max_index]:
                # Minumum number is between min and max
                # Find the middle - Adding 1 since we start from 0
                middle = (min_index + max_index) // 2 + 1
                logging.debug("min_index = {}, max_index = {}, nums[min_index] = {}, nums[max_index] = {}, middle = {}, nums[middle] = {}".format(
                     min_index, max_index, nums[min_index], nums[max_index], middle, nums[middle]))                
                if nums[min_index] > nums[middle]:
                    # The least number is between min_index and middle as min_index is greater than middle
                    max_index = middle
                    min_index = min_index + 1
                else:
                    # min_index is lesser than or equal to middle, which implies the smaller number is between middle and max
                    min_index = middle
                    max_index = max_index
                logging.debug("   min_index = {}, max_index = {}, nums[min_index] = {}, nums[max_index] = {}, middle = {}, nums[middle] = {}".format(
                     min_index, max_index, nums[min_index], nums[max_index], middle, nums[middle]))   
                continue
            return nums[min_index]
        
if __name__ == '__main__':
    s = Solution()
    # rotatedList = [4,5,6,7,0,1,2]
    # minNum = s.findMin(rotatedList)
    # print("The min of {} is {}".format(rotatedList, minNum))

    # rotatedList = [2,1]
    # minNum = s.findMin(rotatedList)
    # print("The min of {} is {}".format(rotatedList, minNum))    

    rotatedList = [3,4,5,1,2]
    minNum = s.findMin(rotatedList)
    print("The min of {} is {}".format(rotatedList, minNum))    
