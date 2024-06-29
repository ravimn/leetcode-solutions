"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * (10**4)
s consists of English letters, digits, symbols and spaces.
"""
import logging

logger = logging.getLogger(__name__)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        debug = False
        if s is None or len(s) == 0: 
            return 0

        charMap = {}
        length = 0
        longest = 0

        for i in s:
            if i in charMap:
                
                matchIndex = charMap[i]

                #if debug : 
                #    print ("Found a match.  Re-adjusting lenghts. -> ", i)
                logger.debug("Found a match.  Re-adjusting lenghts. -> ", i)
                for key in list(charMap.keys()):
                    if (charMap[key] <= matchIndex):
                        #if debug: 
                        #    print ("Deleting ", key)
                        logging.debug("Deleting ", key)
                        del charMap[key]
                    else:
                        charMap[key] = charMap[key] - matchIndex
                        logger.debug(key, '->', charMap[key])
                        logger.debug('charMap is ', charMap)
                        #if debug: 
                        #    print (key, '->', charMap[key])
                        #    print (charMap)

                length = length - matchIndex + 1
                
                charMap[i] = length
                logger.debug(i, '->', length)
                logger.debug('charMap is ', charMap)
            else:
                charMap[i] = length = length + 1
                logger.debug(i, '->', length)
                logger.debug('charMap is ', charMap)

            longest = length if longest < length else longest

        return longest

if __name__ == '__main__':
# Create a logger
    logger = logging.getLogger('example_logger')
    logger.setLevel(logging.DEBUG)  # Set the base logging level for the logger

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Set the logging level for the handler

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    s = Solution()
    string = "abcabcbb"
    longest = s.lengthOfLongestSubstring(string)
    logging.info("Longest substring for string {} is {}".format(string, longest))


