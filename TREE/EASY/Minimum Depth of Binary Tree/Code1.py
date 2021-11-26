# PROBLEM LINK:- https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        
        if l == 0:
            return 1 + r
        elif r == 0:
            return 1 + l
        return 1 + min(l, r)
