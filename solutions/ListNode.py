"""
Definition for singly-linked list.
"""
class ListNode:
    # Constructor method
    # val - default value is 0
    # next - ListNode (Default: None)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Alternate Constructor using an Integer List
    @classmethod
    def from_intList(cls, lists:list[int]):
        if not lists:
            return cls()
        
        first = temp = cls()
        for n in lists:
            t = cls(n)
            temp.next = t
            temp = temp.next
        
        return first.next

    # String value for printing the entire ListNode 
    def __str__(self):
        s = "[" + str(self.val)
        nextL = self.next
        while nextL:
            s = s + "," + str(nextL.val)
            nextL = nextL.next
        s = s + "]"
        return s
