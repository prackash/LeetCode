from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if self.depth(root.left) == self.depth(root.right):
            return root
        if self.depth(root.left) > self.depth(root.right):
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    value=Solution().lcaDeepestLeaves(root)  # Output: 2
    print(value.val if value else None)
    print(value.left.val if value.left else None)
    print(value.right.val if value.right else None)
    