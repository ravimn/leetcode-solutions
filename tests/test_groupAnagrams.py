import pytest
from solutions.groupAnagrams import Solution as groupAnagrams

class TestGroupAnagrams:
    @pytest.mark.parametrize("input, expected", [
        (["eat","tea","tan","ate","nat","bat"],[["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ])
    def test_groupAnagrams(self, input, expected):
        s = groupAnagrams()
        assert s.groupAnagrams(input) == expected