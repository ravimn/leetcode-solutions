"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # Filter candidates to include numbers that are lesser than or equal to target
        candidates = [x for x in candidates if x<= target]
        # Sort candidates for easy retrival - Not sure if this is required
        candidates.sort()
        #Create a new Result list
        result = []

        length = len(candidates)

        def findCombination(index:int, new_target:int, curr_combination: list[int]):
            #Return if Index is greater than or equal to the candidates length
            if index >= length:
                return
            
            # You will never reach the target if the sum of the remaining elements dont add up to the new_target
            if sum(candidates[index:]) < new_target:
                return
            
            # If current combination + new item at index is equal add to resultset
            if sum(curr_combination) + candidates[index] == target:
                result.append(curr_combination + [candidates[index]])

            if candidates[index] < new_target:
                findCombination(index+1, new_target - candidates[index], curr_combination + [candidates[index]])

            # find the index of the number != current number @ current index
            y = 1
            while index + y < length and candidates[index] == candidates[index + y]:
                y += 1
            
            findCombination(index + y, new_target, curr_combination)

        findCombination(0,target, [])
        return result

    def combinationSum3(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(nums,remaining,start_index,path):

            if remaining==0:
                result.append(path[:])
                return          
            
            for i in range(start_index,len(nums)):
                #Dedupe
                if i>start_index and nums[i]==nums[i-1]:
                    continue
                #Prune
                if nums[i]>remaining:
                    break

                dfs(nums,remaining-nums[i],i+1,path+[nums[i]])
        
        candidates.sort()
        result=[]
        dfs(candidates,target,0,[])
        return result
    
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))


    