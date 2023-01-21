import pytest
from solutions.maxPoints import Solution as maxPoints

class TestMaxPoints:
    @pytest.mark.parametrize("points, expected", [
        ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4)
    ])
    def test_maxPoints(self, points, expected):
        r = maxPoints()
        assert r.maxPoints(points) == expected
        