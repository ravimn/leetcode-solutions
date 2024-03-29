"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
Intuition
    The initial thought was to create an hashMap of items and iterate over each item. For each item increment the count and find if its in the hashMap. Return the largest count.

Approach
The initial approach was slow. To improve the efficiency, for each item, I had to iterate both backwards and forward. While doing so, maintain a map of visited items so I dont have to iterate over those items again. This approach is something like picking a thread. Dosen't matter which element of the thread you are picking, you can get the length of the thread. Finally, return the length of the largest thread.

Complexity
Time complexity:
O(n)

Space complexity:
O(n)
"""
class Solution:
    def longestConsecutive(self, nums:list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums_set = set(nums)

        longest = 1; visited = set([])
        for i in nums:
            if i in visited:
                continue
            visited.add(i)
            
            seq_length = 1; j = 1; k = 1
            while (i+j) in nums_set:
                visited.add(i+j)
                j += 1
            while (i - k) in nums_set:
                visited.add(i-k)
                k += 1
            seq_length = j + k - 1

            longest = max(seq_length, longest)

        return longest
        