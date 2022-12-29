import pytest
from solutions.RomanToInt import Solution as romanToInt

"""
Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

#class TestRomanToInt:
@pytest.mark.parametrize("test_input,expected", [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)])
def test_romanToInt(test_input, expected):
    s = romanToInt()
    assert s.romanToInt(test_input) == expected