#Maximum diameter of tree
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left:'Optional[TreeNode]'=0, right:'Optional[TreeNode]'=0):
        self.val = val
        self.left = left 
        self.right = right
class Solution():
    def dim(self, root:Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        dfs(root)
        return self.res

if __name__== "__main__":
    root= TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right  = TreeNode(7)
    sol = Solution()
    print("Diameter of the binary tree is",sol.dim(root))