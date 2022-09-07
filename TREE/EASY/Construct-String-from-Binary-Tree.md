## [Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)

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
    string tree2str(TreeNode* root) {
        if (!root) return "";
        string s = to_string(root->val);
        
        if (!root->left && !root->right) s += "";  
        if (root->left) s += "(" + tree2str(root->left) + ")";
        if (!root->left && root->right) s += "()";
        if (root->right) s += "(" + tree2str(root->right) + ")";
        return s;
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ''
        s = str(root.val)
        
        if not root.left and not root.right: s += ''
        if root.left: s += '(' + self.tree2str(root.left) + ')'
        if not root.left and root.right: s += '()'
        if root.right: s += '(' + self.tree2str(root.right) + ')'
        
        return s
```
