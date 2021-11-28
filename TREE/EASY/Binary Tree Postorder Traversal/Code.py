# PROBLEM LINK:- https://leetcode.com/problems/binary-tree-postorder-traversal/

class Solution:
    def postorder(self, root, v):
        if not root:
            return
        
        self.postorder(root.left, v)
        self.postorder(root.right, v)
        v.append(root.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        v = []
        self.postorder(root, v)
        return v
