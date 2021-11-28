# PROBLEM LINK:- https://leetcode.com/problems/binary-tree-preorder-traversal/
    
class Solution:
    def preorder(self, root, v):
        if not root:
            return
        
        v.append(root.val)
        self.preorder(root.left, v)
        self.preorder(root.right, v)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        v = []
        self.preorder(root, v)
        return v  
