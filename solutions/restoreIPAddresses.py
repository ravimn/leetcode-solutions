"""
A valid IP address consists of exactly four integers separated by single dots. 
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, 
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, 
return all possible valid IP addresses that can be formed by inserting dots into s. 
You are not allowed to reorder or remove any digits in s. 
You may return the valid IP addresses in any order.

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.

Approach:


"""
class Solution:

    def isValidIPv4Part(self, s:str) -> bool:
        print("isValidIPv4Part - " + s)
        if not s.isnumeric():
            return False       
        if len(s) == 0 or len(s) > 3:
            return False        
        if len(s) == 1:
            return True        
        if s[0] == '0':
            return False        
        if int(s) < 256:
            return True        
        return False
    
    def returnIPAddress(self, parts: list[str]) -> str:
        if len(parts) != 4:
            return ""       
        return '.'.join(str(ipPart) for ipPart in parts)
    
    def getIpAddresses(self, s: str, startIndex: int, parts: list[str], ans: list[str]):
        # Given a string length and number of parts left return any condition that will not make the rest of the IP Parts
        print("getIPAddressess s [" + s + "] startIndex [" + str(startIndex) + "] parts [" + str(parts) + "] ans [" + str(ans) + "]")
        if (startIndex >= len(s)):
            return
        if len(s[startIndex:]) < 4 - len(parts):
            return
        if len(s[startIndex:]) > (4 - len(parts))*3:
            return
        if (len(parts) == 3):
            lastPart = s[startIndex:len(s)]
            isLastPartValid:bool = self.isValidIPv4Part(lastPart)

            if (isLastPartValid):
                parts.append(lastPart)
                ans.append(self.returnIPAddress(parts))
                print ("Answer is " + str(ans))
                parts.pop()
            return
        
        for x in range(3):
            part = s[startIndex:startIndex+x+1]
            if (self.isValidIPv4Part(part)):
                parts.append(part)
                self.getIpAddresses(s, startIndex+x+1, parts, ans)
                #backtracking - removing the earlier part from parts array
                parts.pop()
        
    def restoreIpAddresses(self, s: str) -> list[str]:
        parts:list[str] = []
        ans: list[str] = [] 
        self.getIpAddresses(s, 0, parts, ans)
        print( "Answer is [" + str(ans) + "]")
        return ans