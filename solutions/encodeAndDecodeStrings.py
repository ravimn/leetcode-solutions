"""
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear

Do not rely on any libraries, the purpose of this problem is to implement the "encode" and "decode" algorithms on your own
Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""
class Solution:
    DELIM = '#'
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs:list[str]) -> str:
        # write your code here
        ret = ''
        for s in strs:
            ret = ret + self.getEncodedString(s)
        return ret
    
    def getEncodedString(self, s:str) -> str:
        ret_s = ''
        j = 0
        while j < len(s):
            index = s.find(self.DELIM, j)
            if index == -1:
                ret_s = ret_s + s[j:]
                break
            else:
                ret_s = ret_s + s[j:index+1] + self.DELIM
                j = index + 1
        return ret_s + self.DELIM


    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, s:str) -> list[str]:
        ret = []
        start = 0; temp = ''
        length = len(s)
        while start < length:
            delim_index = s.find(self.DELIM, start)
            if delim_index == -1:
                # This scenario can never occur.  The last char of the string has to be the delimiter
                return ret
            
            if delim_index == length - 1:
                # You have reached the end of the string.  Add the last string to return list
                ret.append(temp + s[start:length - 1])
                return ret  
            
            if s[delim_index + 1] == self.DELIM:
                temp = temp + s[start:delim_index+1]
                start = delim_index + 2
            else:
                ret.append(temp + s[start:delim_index])
                temp = ''
                start = delim_index + 1
        
        return ret
            
        