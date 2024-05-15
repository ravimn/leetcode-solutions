"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from vo.Node import Node
from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        current = head
        while current:
            new_current = Node(current.val, current.next, current.random)
            current.next = new_current
            current = current.next.next

        
        # Lets fix random first
        current = head
    
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        #Lets fix the next pointers
        current = head
        new_head = new_current = head.next
        while current.next.next:
            current.next = current.next.next
            new_current.next = new_current.next.next

            current = current.next
            new_current = new_current.next
        
        return new_head
    
if __name__ == '__main__':
    node_list = []
    node_list.append(Node(7, None, None))
    node_list.append(Node(13, None, None))
    node_list.append(Node(11, None, None))
    node_list.append(Node(10, None, None))
    node_list.append(Node(1, None, None))

    l = len(node_list)
    for n in range(l-1):
        node_list[n].next = node_list[n+1]
    
    node_list[0].random = None
    node_list[1].random = node_list[0]
    node_list[2].random = node_list[4]
    node_list[3].random = node_list[2]
    node_list[4].random = node_list[0]

    s = Solution()
    head = node_list[0]
    new_head = s.copyRandomList(head)
    print("new_head is {}".format(new_head))




