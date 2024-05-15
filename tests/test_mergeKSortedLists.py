import unittest
from solutions.linkedlist.mergeKSortedLists import Solution
from solutions.linkedlist.vo.ListNode import ListNode

class TestMergeKLists(unittest.TestCase):
    def setUp(self) -> None:
        self.Solution = Solution()

    def test_mergeKLists_heapq(self):
        inlist = [ListNode.from_intList([1,3,5]), ListNode.from_intList([2,4,6])]
        outlist = [1, 2, 3, 4, 5, 6]
        self.assertEqual(str(self.Solution.mergeKListsWithHeapQ(inlist)), str(ListNode.from_intList(outlist)))
