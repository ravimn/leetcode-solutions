from typing import Optional
from ListNode import ListNode
from mergeLists import Solution as mergeList

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        mlSolution = mergeList()

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        i = 1
        finalList = lists[0]
        while i < len(lists):
            finalList = mlSolution.mergeTwoLists(finalList, lists[i])
            i = i + 1

        return finalList
