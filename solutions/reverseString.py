class Solution:
    def reverseString(self, s:str) -> str: 
        if len(s) == 1:
            return s
        
        return self.reverseString(s[1:]) + s[0]

    