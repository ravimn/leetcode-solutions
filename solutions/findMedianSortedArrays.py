"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x = len(nums1)
        y = len(nums2)
        if x > y :
            return self.findMedianSortedArrays(nums2, nums1)
        start = 0
        end = x
        isFound = False
        isEven = True if (x+y) % 2 == 0 else False
        
        MIN = -10**7
        MAX = 10**7

        while start <= end:
            partitionX = (start + end) // 2
            partitionY = ((x + y + 1) // 2) - partitionX

            maxLeftX = MIN if partitionX == 0 else nums1[partitionX - 1]
            minRightX = MAX if partitionX == x else nums1[partitionX]

            maxLeftY = MIN if partitionY == 0 else nums2[partitionY - 1]
            minRightY = MAX if partitionY == y else nums2[partitionY]

            if (maxLeftX <= minRightY and maxLeftY <= minRightX) :
                if isEven is True :
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else :
                    return max(maxLeftX, maxLeftY)

                # return value
            else:
                if maxLeftX > minRightY :
                    end = partitionX - 1
                else :
                    start = partitionX + 1