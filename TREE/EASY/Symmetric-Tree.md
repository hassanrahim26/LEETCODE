## [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

* **C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool solve(TreeNode* root1, TreeNode* root2){
        if(root1 == NULL && root2 == NULL)
            return true;
        
        else if(root1 == NULL || root2 == NULL || root1->val != root2->val)
            return false;
        
        return solve(root1->left, root2->right) && solve(root1->right, root2->left);
    }
    
    bool isSymmetric(TreeNode* root) { 
        return solve(root, root);
    }
};
```

* **PYTHON**
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        
        elif root1 == None or root2 == None or root1.val != root2.val:
            return False
        
        return self.solve(root1.left, root2.right) and self.solve(root1.right, root2.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root, root)
```
