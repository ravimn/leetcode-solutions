"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""
"""
It took some time (about 3 weeks for me to solve the problem)
My first iteration included making a copy of the current-combination and candidates.  It worked tough.
The combination of copying an array at every recursive step proved to be too costly.
The same # of recursive steps wihtout any additional copying is what resulted in the below code in addition to some help from Leetcode

The solution from what is laid out here uses DFS method.

This code defines a class Solution with a method combinationSum that finds all unique combinations of integers from a given list (candidates) that sum up to a target value (target). It does so using a backtracking approach:

Initialize an empty list result to store the valid combinations.
Filter the candidates list to contain only elements less than or equal to the target, and sort it.
Define a recursive function findCombinations that explores all possible combinations.
Inside findCombinations:
Check if the current index exceeds the length of the candidates list; if so, return.
Check if the remaining target equals the current candidate; if so, append the current combination to the result list.
If the remaining target is greater than the current candidate, recursively call findCombinations with the updated target (subtracting the current candidate) and update the current combination by appending the current candidate.
Recursively call findCombinations without including the current candidate in the combination.
Return the result list containing all unique combinations.
This method efficiently finds combinations that sum up to the target by exploring all possibilities using recursion and backtracking. However, it may produce duplicate combinations if the candidates list contains duplicates.
"""
class Solution:
    def combinationSum(self, candidates:list[int], target:int) -> list[list[int]]:
        result = []
        candidates = [x for x in candidates if x <= target]
        candidates.sort()
        length = len(candidates)

        def findCombinations(new_target:int, index:int, curr_combination:list[int]):
            #print( "."*tabcount + "findCombinations - new_target [" + str(new_target) + "] index " + str(index) + " curr_combination " + str(curr_combination) )            

            if index >= length:
                return
            
            if new_target == candidates[index]:
                result.append(curr_combination + [candidates[index]])

            if new_target > candidates[index]:
                findCombinations(new_target - candidates[index], index, curr_combination + [candidates[index]])

            findCombinations(new_target, index + 1, curr_combination)
  
        findCombinations(target, 0, [])
        return result