# PROBLEM LINK:- https://leetcode.com/problems/symmetric-tree/

class Solution:
    def solve(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        
        elif root1 == None or root2 == None or root1.val != root2.val:
            return False
        
        return self.solve(root1.left, root2.right) and self.solve(root1.right, root2.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root, root)
