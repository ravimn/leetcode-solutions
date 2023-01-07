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

