import pytest
from solutions.isPalindrome import Solution as isPalindrome

class TestIsPalindrome:
    @pytest.mark.parametrize("input, expected", [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ])
    def test_isPalindrome(self, input:str, expected:bool):
        s = isPalindrome()
        assert s.isPalindrome(input) == expected