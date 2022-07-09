## [Evaluate Boolean Binary Tree](https://leetcode.com/problems/evaluate-boolean-binary-tree/)

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
    bool evaluateTree(TreeNode* root) {
        if(!root->left and !root->right)    
            return root->val;
        
        bool l = evaluateTree(root->left);
        bool r = evaluateTree(root->right);
        
        if(root->val == 2)
            return l or r;
        return l and r;
    }
};
```

* **Python**
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val
        
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        
        if root.val == 2:
            return l or r
        return l and r
```
