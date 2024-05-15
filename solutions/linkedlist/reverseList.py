"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

Approach:
Iterate over the list
if head is None -> exit
else 
temp = head.next
head.next = head
head = temp
"""
from typing import Optional
from vo.ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        next_node = head.next
        head.next = None
        while next_node is not None:
            temp_next = next_node.next
            next_node.next = head
            head = next_node
            next_node = temp_next

        return head
    
    def reverseListRecursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        def reverse(prior: ListNode, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return prior
            current = head
            head = head.next
            current.next = prior
            return reverse(current, head)
        
        return reverse(ListNode(head.val, None), head.next)

            
    
if __name__ == '__main__':
    head = ListNode.from_intList([1,2,3,4,5])
    s = Solution()
    new_list = s.reverseListRecursion(head)
    print(new_list)