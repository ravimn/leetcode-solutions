import pytest
from solutions.containsDuplicates import Solution as containsDuplicates

class TestContainsDuplicates:
    @pytest.mark.parametrize("input, expected", [
        ([1,2,3,1],True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True), 
        ([1,1], True)
    ])
    def test_containsDuplicates(self, input, expected):
        s = containsDuplicates()
        assert s.containsDuplicate(input) == expected