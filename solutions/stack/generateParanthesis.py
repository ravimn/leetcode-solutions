"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""
class Solution:
    def generateParenthesis(self, n) -> list[str]:
        """
        :type n: int
        :rtype: List[str]
        """
        rList = []        
        if n == 1:
            rList.append("()")
            return rList

        xList = self.generateParenthesis(n-1)
        for x in xList:
            self.addList('(' + x + ')', rList)
            self.addList(x + '()', rList)
            self.addList('()' + x, rList)
        
        if (n % 2) == 0:
            llist = self.generateParenthesis(n/2)
            for x in llist:
                for y in llist:
                    self.addList(x+y, rList)

            return rList
        
    def addList(self, x, rList):
        if x not in rList:
            rList.append(x)
    
    def generateParanthesis_bt(self, n:int) -> list[str]:
        result = []
        def backtracing(lCnt:int, rCnt:int, pStr:str) -> None:
            if lCnt == n and rCnt == n:
                result.append(pStr)
                return
            
            if lCnt < n:
                lCnt += 1
                backtracing(lCnt, rCnt, pStr+"(")
                lCnt -= 1
            
            if rCnt < lCnt:
                rCnt += 1
                backtracing(lCnt, rCnt, pStr+')')
                rCnt -= 1
        
        backtracing(0,0,'')
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.generateParanthesis_bt(3))

            