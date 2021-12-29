# PROBLEM LINK:- https://leetcode.com/problems/balanced-binary-tree/

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        return 1 + max(lh, rh)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        if (abs(lh - rh) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False
