"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


"""
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        fMap = defaultdict(int)
        for n in nums:
            fMap[n] += 1

        countMap = defaultdict(list)
        for n, count in fMap.items():
            countMap[count].append(n)

        result = []
        m = 0
        sorted_count_list = list(countMap.keys())
        sorted_count_list.sort(reverse=True)
        for count in sorted_count_list:
            cList = countMap[count]
            l = len(cList)
            result.extend(cList)
            m = m+l
            if m >= k:
                break

        return result[:k]

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))