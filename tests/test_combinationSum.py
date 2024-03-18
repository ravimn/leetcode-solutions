import pytest
from solutions.combinationSum import Solution as combinationSum

class TestCombinationSum:
    @pytest.mark.parametrize("candidates, target, expected", [
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, []),
        ([3,5,8], 11, [[3,8],[3,3,5]])
    ])
    def test_combinationSum(self, candidates, target, expected):
        r = combinationSum()
        assert r.combinationSum(candidates, target) == expected
        