import heapq
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

    def mergeKListsWithHeapQ(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mylist = [(list[i][0], i, 0) for i in range(len(lists))]

        heapq.heapify(mylist)
        mergeList = []

        while(mylist):
            (val, listindex, elementindex) = heapq.heappop(mylist)
            mergeList.append(val)

            if (elementindex + 1 < len(lists[listindex])):
                heapq.heappush(mylist, (lists[listindex][elementindex + 1], listindex, elementindex + 1))

        return ListNode.from_intList(mergeList)

