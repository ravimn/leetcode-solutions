"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


from typing import Optional
from vo.ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp_c = finalLL = ListNode(0)
        tmp_a = l1
        tmp_b = l2
        carryOver = False
        
        while (tmp_a or tmp_b):
            if not tmp_a: 
                tmp_a = ListNode(0)
            if not tmp_b:
                tmp_b = ListNode(0)

            valA = tmp_a.val if tmp_a else 0
            valB = tmp_b.val if tmp_b else 0
            valC = tmp_c.val if tmp_c else 0

            s = valA + valB + valC
            value = s % 10

            d = s // 10
            if d > 0 : 
                carryNode = ListNode(1)
            else:
                if (tmp_a.next is None and tmp_b.next is None):
                    carryNode = None
                else:
                    carryNode = ListNode(0)


            #print ("Added value is ", value, tmp_c, finalLL)

            if (tmp_c):
                tmp_c.val = value 
                tmp_c.next = carryNode
            else:
                tmp_c = ListNode(value, carryNode)

            tmp_a = tmp_a.next if tmp_a else None
            tmp_b = tmp_b.next if tmp_b else None
            tmp_c = tmp_c.next if tmp_c else None
        
        return finalLL