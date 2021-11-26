# PROBLEM LINK:- https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
    def inorder(self, root, v):
        if not root:
            return
        
        self.inorder(root.left, v)
        v.append(root.val)
        self.inorder(root.right, v)
            
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        v = []
        self.inorder(root, v)
        return v
