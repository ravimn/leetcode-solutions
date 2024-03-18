class Solution:
    def letterCombinations(self, digits:str) -> list[str]:

        dmap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9': 'wxyz'}
        res = []
        
        if digits == '':
            return res
        
        def getCombinations(index, combination, digits, res):
            if len(combination) == len(digits):
                res.append(combination)
                return
            for i in dmap.get(digits[index]):
                getCombinations(index + 1, combination + i, digits, res)

        getCombinations( 0, '', digits, res)
        return res




