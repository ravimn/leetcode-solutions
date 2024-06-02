"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * (10**4)
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        debug = False
        if s is None or len(s) == 0: 
            return 0

        charMap = {}
        length = 0
        longest = length

        for i in s:
            if i in charMap:
                
                matchIndex = charMap[i]

                #if debug : 
                #    print ("Found a match.  Re-adjusting lenghts. -> ", i)
                for key in list(charMap.keys()):
                    if (charMap[key] <= matchIndex):
                        #if debug: 
                        #    print ("Deleting ", key)
                        del charMap[key]
                    else:
                        charMap[key] = charMap[key] - matchIndex
                        #if debug: 
                        #    print (key, '->', charMap[key])
                        #    print (charMap)

                length = length - matchIndex + 1
                
                charMap[i] = length
                #if debug:
                #    print (i, '->', length)
                #    print (charMap)
            else:
                charMap[i] = length = length + 1
                #if debug:
                #    print (i, '-->', charMap[i]) 
                #    print (charMap) 

            longest = length if longest < length else longest

        return longest

