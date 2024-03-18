import pytest

from solutions.findShortestSubArray2 import Solution as findShortestSubArray

class TestFindShortestSubArray:

    @pytest.mark.parametrize("nums, expected", [
        ([1,2,2,3,1], 2),
        ([1,2,2,3,1,4,2], 6),
    ])
    def test_findShortestSubArray(self, nums:list[int], expected:int):
        r = findShortestSubArray()
        assert r.findShortestSubArray(nums) == expected