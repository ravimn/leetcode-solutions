"""
Search for a given number in a sorted list of numbers.  Search with O(log n) complexity

return -1 if number not found


"""
class Solution:
    def binarySearch(self, nums: list[int], n: int) -> bool:
        start = 0
        end = len(nums) - 1

        #while (start <= end and start >= 0 and end < len(nums)):
        while start <= end:
            x = (start + end) // 2
            if (n == nums[x]):
                return True

            if n < nums[x]:
                end = x - 1
            else:
                start = x + 1
        
        return False


