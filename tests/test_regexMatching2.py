import pytest
from solutions.regexMatching2 import Solution as regexMatching

class TestRegexMatching:
    @pytest.mark.parametrize("text, pattern, expected", [
        ("aa", "a", False), 
        ("aa", "a*", True), 
        ("ab", ".*", True), 
        ("aab", "c*a*b", True),
        ("caab", "c*a*b", True),
        ("caabc", "c*a*b", False),
        ("aaa", "a*a", True),
        ])
    def test_regexMatching(self, text, pattern, expected):
        r = regexMatching()
        assert r.isMatchRecursion(text, pattern) == expected
        