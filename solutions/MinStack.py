"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""
class Node:
    def __init__(self, val: int, min: int):
        self.val = val
        self.min = min

class MinStack:

    def __init__(self):
        self.stack:list[Node] = []
        self.min = None
        

    def push(self, val: int) -> None:
        self.stack.append(Node(val, self.min))
        if self.min == None or self.min > val:
            self.min = val
        
        

    def pop(self) -> None: 
        n:Node = self.stack.pop()
        if n == None:
            self.min = None
        self.min = n.min
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        
        n:Node = self.stack[-1]
        return n.val
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()