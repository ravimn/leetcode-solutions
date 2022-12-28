import heapq
from typing import Optional
from solutions.ListNode import ListNode
from solutions.mergeLists import Solution as mergeList

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

    def mergeKListsWithHeapQ(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mylist = [(lists[i].val, i) for i in range(len(lists))]

        heapq.heapify(mylist)
        mergeList = []

        while(mylist):
            (val, listindex) = heapq.heappop(mylist)
            mergeList.append(val)
            lists[listindex] = lists[listindex].next
            if lists[listindex]:
                heapq.heappush(mylist, (lists[listindex].val, listindex))

        return ListNode.from_intList(mergeList)

