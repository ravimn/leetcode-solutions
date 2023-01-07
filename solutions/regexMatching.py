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
Split regular expressions by the number of literals
classify each literal 
actual match -> constant
. -> any char
* -> 0 to n until actual match

move forward by regular expression
new match
if literal 
   match string with literal.  if not match return false else move to next match and trim string
if . 
    match string with any char
if *
    move to next regular expression that is not * or .
    have a counter for every .
    get the next literal
    if no literal found len(remaing string) should be >= 

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "*":
            return True
        
        if p == "." and len(s) == 1:
            return True

        if s == p:
            return True

        if not p and not s:
            return True
        
        if s and not p:
            return False
        
        if len(p) == 1 and len(s) == 1 and p != s:
            return False

        isStarPattern = False
        pattern = p[0]
        if pattern != "*":
            if (self.isMatch(s[0], pattern)):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        
        # pattern is eq "*"
        isStarPattern = True
        #check if last pattern is *
        if p[-1] == "*":
            return self.isRegexMatch(s, p[1:len(p)-1])

        return self.isMatch(s[::-1], p[::-1])

    def isRegexMatch(self, s: str, p: str) -> bool:
        if p == "*":
            return True
        
        if p == "." and len(s) >= 1:
            return True

        if s == p:
            return True

        if not p and not s:
            return True
        
        if s and not p:
            return True
        
        if len(p) == 1 and len(s) == 1 and p != s:
            return False

        dotBeforeLiteral = 0
        literalFoundinPattern = False
        while p:
            l = p[0]
            if l == ".":
                dotBeforeLiteral += 1
                p = p[1:]
                continue
            if l == "*":
                p = p[1:]
                continue

            #found a literal
            literalFoundinPattern = True

            literalFoundinStr = False
            #find position of l in string s
            for i in range(len(s)):
                if s[i] == l:
                    literalFoundinStr = True
                    break
            if not literalFoundinStr:
                return False
            else:
                if (dotBeforeLiteral > i):
                    return False
                
                #Found a partial substring match till the first literal pattern
                #Send rest of pattern adding a * in the end with a full match with rest of string
                p = p[i+1:] + "*"
                return self.isMatch(s[i+1:], p)

            



