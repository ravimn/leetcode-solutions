import pytest
from solutions.maxArea import Solution as maxArea

class TestContainerWithMostWater:
    @pytest.mark.parametrize("input, expected_value", [
        ([],0),
        ([100], 0),
        ([1,8,6,2,5,4,8,3,7], 49), 
        ([1,1], 1), 
        ([1,2,3,4], 4)])
    def test_maxArea(self, input, expected_value):
        s = maxArea()
        assert s.maxArea(input) == expected_value