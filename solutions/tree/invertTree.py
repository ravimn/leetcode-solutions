from typing import Optional
from vo.TreeNode import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.invertNode(root)
        return root
        
    def invertNode(self, node: Optional[TreeNode]):
        if node is None:
            return

        temp = node.left
        node.left = node.right
        node.right = temp

        self.invertNode(node.left)
        self.invertNode(node.right)
