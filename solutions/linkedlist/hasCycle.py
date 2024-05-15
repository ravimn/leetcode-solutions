from typing import Optional
from vo.ListNode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        one = two = head

        isLoop = False
        while two.next and two.next.next:
            one = one.next
            two = two.next.next

            if one == two:
                isLoop = True
                break

        return isLoop
    
if __name__ == '__main__':
    node_list = []
    node_list.append(ListNode(3))
    node_list.append(ListNode(2))
    node_list.append(ListNode(0))
    node_list.append(ListNode(-4))

    for i in range(len(node_list) - 1):
        node_list[i].next = node_list[i+1]
    
    node_list[-1].next = node_list[1]

    s = Solution()
    isCycle = s.hasCycle(node_list[0])
    print("Is Cycle " + str(isCycle))

            
