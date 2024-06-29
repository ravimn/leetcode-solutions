"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:

Input: piles = [1,4,3,2], h = 9

Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:

Input: piles = [25,10,23,4], h = 4

Output: 25
Constraints:

1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000
"""
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the log level to DEBUG to capture all types of log messages
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Specify the log message format
    handlers=[
#        logging.FileHandler('app.log'),  # Log messages to a file named 'app.log'
        logging.StreamHandler()  # Also log messages to the console
    ]
)

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_speed = max(piles)
        min_speed = 1
        x = 0
        n = 0
        while min_speed <= max_speed:
            x = (min_speed + max_speed) // 2
            hours = self.getEatingHours(piles, x)
            logging.debug("x = {}, min_speed = {}, max_speed = {}, hours = {}".format(x, min_speed, max_speed, hours))
            
            if hours > h:
                min_speed = x + 1
            else:
                n = x
                max_speed = x - 1

        return n

    def getEatingHours(self, piles: list[int], speed: int) -> int:
        hours = 0
        for p in piles:
            hours += p // speed
            if p % speed != 0:
                hours += 1 
        return hours
    
if __name__ == '__main__':
    s = Solution()
    h = s.minEatingSpeed([1, 4, 3, 2], 9)
    print("number of Bananas to be eaten per hour is {}".format(h))
    h = s.minEatingSpeed([25,10,23,4], 4)
    print("number of Bananas to be eaten per hour is {}".format(h))