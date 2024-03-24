"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
"""
Solution Approach
1. Initially I thought of using a alphabet to number map and calculate the sum of each string.  Finding the sum of the string and grouping them in a hashmap of the sum to its list of strings.  The approach worked as long as there were no duplicates in the string.  If there were duplicates, the sum could match with sum of some other string For e.g. ill, duh.
2. I had to then pivot to using a sorted function on the string iterable.  I initally used a for loop.  I then used chatGpt to give me an answer with lambda function.  Interstingly, chatGPT's answer didn't work in python3 as I need to force a list operation on the map operation.  I have to however thank chatGPT for showing me defaultdict instead of dict.  Made my code really concise.
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
        stringSortMap = defaultdict(list)
        # for s in strs:
        #     stringSortMap[''.join(sorted(s))].append(s)
        
        _ = list(map(lambda s: stringSortMap[''.join(sorted(s))].append(s), strs))

        return list(stringSortMap.values())   




