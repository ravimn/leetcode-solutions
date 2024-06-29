"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

"""
from solutions.binarySearch.binarySearch import Solution as binarySearch
class Solution:

    def searchMatrix(self, matrix:list[list[int]], target: int) -> bool:
        bs = binarySearch()
        start = 0
        end = len(matrix) - 1

        #while (start <= end and start >= 0 and end < len(nums)):
        while start <= end:
            x = (start + end) // 2
            if matrix[x][0] <= target <= matrix[x][-1]:
                return bs.binarySearch(matrix[x], target) 
            
            if target < matrix[x][0]:
                end = x - 1 
            else:
                start = x + 1

        return False
        
if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1],[3],[5]], 1))
            


