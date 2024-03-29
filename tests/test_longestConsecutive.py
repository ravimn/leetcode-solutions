import pytest
from solutions.longestConsecutive import Solution as longestConsecutive

class TestLongestConsecutive:
    @pytest.mark.parametrize("input, expected", [
        ([100, 3, 200, 4, 1, 2], 4),
        ([3,1,2,4,8,9,5,6,7], 9),
    ])
    def test_longestConsecutive(self, input:list[int], expected:int):
        s = longestConsecutive()
        assert s.longestConsecutive(input) == expected
    