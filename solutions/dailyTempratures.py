"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. If there is no future day for which this is 
possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        result = [0]*length
        stack = []
        # for index, temp in enumerate(temperatures):
        #     if len(stack) == 0:
        #         stack.append((index, temp))
        #     else:
        #         top_idx, top_temp = stack[-1]
        #         if temp <= top_temp:
        #             stack.append((index, temp))
                
        #         while temp > top_temp:
        #             stack.pop()
        #             result[top_idx] = index - top_idx
        #             if len(stack) == 0:
        #                 break
        #             top_idx, top_temp = stack[-1]

        #         stack.append((index, temp))
        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = index - idx
            stack.append(index)
        
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))



