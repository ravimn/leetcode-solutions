from solutions.linkedlist.vo.ListNode import ListNode
from solutions.linkedlist.mergeKSortedLists import Solution
import pytest

@pytest.fixture
def input():
    return [ListNode.from_intList([1,3,5]), ListNode.from_intList([2,4,6])]

@pytest.fixture
def expected():
    return [1,2,3,4,5,6]

class TestMerge:
    def test_MergeKLists(self, input, expected):
        self.Solution = Solution()
        assert str(self.Solution.mergeKListsWithHeapQ(input)) == str(ListNode.from_intList(expected))

