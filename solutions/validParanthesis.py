class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_BRACES = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        CLOSED_BRACES = {
            '}' : 1,
            ')' : 1,
            ']' : 1
        }

        parseQueue = []

        for c in s:
            if c in OPEN_BRACES:
                parseQueue.append(OPEN_BRACES[c])

            if c in CLOSED_BRACES:
                if not parseQueue: return False
                if parseQueue.pop() != c: return False
        
        return len(parseQueue) == 0
    
    def isValidParanthesis(self, s:str) -> bool:
        if s is None:
            return True
        if len(s.strip()) == 0:
            return True
        
        left = 0; right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False


