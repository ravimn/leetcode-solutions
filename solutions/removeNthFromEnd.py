"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?

Approach
Initialize prior = None, current = head, end = None
Have the end pointer move n times
Until end hits None
    prior = current
    current = current.next
    end = end.next

Finally prior.next = current.next
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from vo.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prior = current = end = head
        for i in range(n):
            end = end.next
        
        while end:
            prior = current
            current = current.next
            end = end.next

        if prior == current:
            head = head.next
        else:
            prior.next = current.next

        return head
    
if __name__ == "__main__":
    s = Solution()
    l = s.removeNthFromEnd(ListNode.from_intList([1,2,3]), 3)
    print("Adjusted list is {}".format(l))
