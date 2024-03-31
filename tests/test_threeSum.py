import pytest
from solutions.threeSum import Solution as threeSum

class TestthreeSum:
    @pytest.mark.parametrize("nums, expected", [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], [])
    ])
    def test_threeSum(self, nums:list[int], expected:list[list[int]]):
        r = threeSum()
        assert r.threeSumUsingTwoSum(nums) == expected

    @pytest.mark.parametrize("nums, expected", [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], [])
    ])
    def test_threeSumWithTwoSumTwoPointer(self, nums:list[int], expected:list[list[int]]):
        r = threeSum()
        assert r.threeSumWithTwoSumTwoPointer(nums) == expected

        
        