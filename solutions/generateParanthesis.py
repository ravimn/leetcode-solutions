"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """        
        if n == 1:
            rList = []
            rList.append("()")

            return rList
        else:
            rList = []
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