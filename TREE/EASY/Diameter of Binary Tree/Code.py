# PROBLEM LINK:- https://leetcode.com/problems/diameter-of-binary-tree/

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        ld = self.diameterOfBinaryTree(root.left)
        rd = self.diameterOfBinaryTree(root.right)
        
        return max(lh + rh, max(ld, rd))
