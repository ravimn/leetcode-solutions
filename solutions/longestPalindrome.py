class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        while l > 0 :
            start = 0
            end = l
            while ( start <= len(s) - l):
                t = s[start:end]
                if self.isPalindrome(t) :
                    return t
                start = start + 1
                end = end + 1
            
            l = l - 1

            
    def isPalindrome(self, s:str) -> bool:
        return s == s[::-1]