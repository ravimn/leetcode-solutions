import pytest
from solutions.regexMatching import Solution as regexMatching

class TestRegexMatching:
    @pytest.mark.parametrize("text, pattern, expected", [
        ("aa", "a", False), 
        ("aa", "a*", True), 
        ("ab", ".*", True), 
        ("aab", "c*a*b", False),
        ("caab", "c*a*b", True),
        ("caab", "c**a*b", True),
        ("caab", "c.*a*b", True)])
    def test_regexMatching(self, text, pattern, expected):
        r = regexMatching()
        assert r.isMatch(text, pattern) == expected
        