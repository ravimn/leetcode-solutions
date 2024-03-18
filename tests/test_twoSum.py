import pytest
from solutions.twoSum import Solution as twoSum

class TesttwoSum:
    @pytest.mark.parametrize("nums, target, expected", [
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0,1])
    ])
    def test_twoSum(self, nums, target, expected):
        r = twoSum()
        assert r.twoSum(nums, target) == expected
        