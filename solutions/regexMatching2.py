"""
10. Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

Approach:
Get Next Pattern 
   Parse String until you find a mismatch or end of string

if at the end - you are left with pattern or string return false else return true

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*":
            return True

        p_ptr = 0
        s_ptr = 0 
        while p_ptr < len(p):
            c = p[p_ptr]
            matchOne = True if p_ptr + 1 == len(p) or p[p_ptr+1] != "*" else False

            if matchOne:
                #Match one character.  If ".", match any
                #If there is no more String left to match - return False
                if s_ptr >= len(s):
                    return False

                if c == "." or c == s[s_ptr]:
                    p_ptr += 1
                    s_ptr += 1
                    continue
                else:
                    return False
            else:
                #Match Zero or Many
                while s_ptr < len(s) and (c == "." or c == s[s_ptr]):
                    s_ptr += 1
                #Move pattern pointer by 2 
                p_ptr += 2
        
        return s_ptr == len(s)

    def isMatchRecursion(self, s:str, p: str) -> bool:
        # If pattern is null then return if string is null
        if not p: return not s

        #Match the first character
        matchOne = bool(s) and p[0] in {s[0], '.'}

        #If pattern is only one char return if string greater than 1 char
        if len(p) == 1:
            return matchOne and self.isMatchRecursion(s[1:], p[1:])

        #Check if its not a star pattern
        if (len(p) >= 2 and p[1] != '*'):
            return matchOne and self.isMatchRecursion(s[1:], p[1:])
        else:
            # Match 0 or many
            return (self.isMatchRecursion(s, p[2:])) or ( matchOne and self.isMatchRecursion(s[1:], p))
 

            



