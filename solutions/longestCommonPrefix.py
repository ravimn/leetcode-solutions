class Solution:
    def findShortestLength(self, strs: list[str]) -> int:
        if len(strs) == 0 :
            return 0

        l = len(strs[0])

        for s in strs :
            if l > len(s) :
                l = len(s)
        
        return l
    
    def isCharSame(self, strs: list[str], p: int) -> bool:
        s = strs[0][p]
        for s1 in strs :
            if s != s1[p] :
                return False
        
        return True


    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        l = self.findShortestLength(strs)
        print ("Shortest Length is ", l)
        if l == 0: 
            return ""

        while i < l :
            if self.isCharSame(strs, i) :
                i = i + 1
                continue
            else :
                break
        return strs[0][0:i]

s = Solution()
s.longestCommonPrefix(["","b"])