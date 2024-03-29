import pytest
from solutions.productExceptSelf import Solution as productExceptSelf

class TestProductExceptSelf:
    @pytest.mark.parametrize("nums, expected", [
        ([1,2,3,4], [24, 12, 8, 6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
        ([3],[1]), 
    ])
    def test_productExceptSelf(self, nums: list[int], expected: list[int]):
        s = productExceptSelf()
        assert s.productExceptSelf(nums) == expected