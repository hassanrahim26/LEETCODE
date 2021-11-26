# PROBLEM LINK:- https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if None in [root.left, root.right]:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
