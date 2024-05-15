"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""
from typing import Optional
from vo.ListNode import ListNode
from reverseList import Solution as reverseList


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return
        
        first = head
        (middle, middle_plus_one) = self.findMiddle(head)
        print ("Middle is {}, {}".format(middle, middle_plus_one))
        reverse = reverseList()
        middle_plus_one_reversed = reverse.reverseList(middle_plus_one)
        print("Reverse List is {}".format(middle_plus_one_reversed))
        middle.next = None
        print("first is {}".format(first))

        # We have first and middle_plus_one_reversed
        while (first is not None and middle_plus_one_reversed is not None):
            temp_first = first.next
            temp_middle_plus_one_reversed = middle_plus_one_reversed.next

            first.next = middle_plus_one_reversed
            middle_plus_one_reversed.next = temp_first
            
            first = temp_first
            middle_plus_one_reversed = temp_middle_plus_one_reversed


            



    def findMiddle(self, head:Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]): # type: ignore
        p1 = p2 = head
        while p2 is not None and p2.next is not None and p2.next.next is not None:
            print("Iterating over to find middle")
            p1 = p1.next
            p2 = p2.next.next
        return (p1, p1.next)

if __name__ == "__main__":
    s = Solution()
    head = ListNode.from_intList([1,2,3,4,5,6])
    s.reorderList(head)
    print("head is {}".format(head))