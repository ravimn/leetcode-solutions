import pytest
from solutions.searchInsert import Solution as searchInsert

class TestSearchInsert:
    @pytest.mark.parametrize("nums, target, expected", [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4)
        ])
    def test_searchInsert(self, nums, target, expected):
        r = searchInsert()
        assert r.searchInsert(nums, target) == expected
        