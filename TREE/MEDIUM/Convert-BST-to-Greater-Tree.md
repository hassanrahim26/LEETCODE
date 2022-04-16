## [Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)

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
    int curr_sum;
    void traverse(TreeNode* root)
    {
        if(root->right)
            traverse(root->right);
        
        curr_sum += root->val;
        root->val = curr_sum;
        
        if(root->left)
            traverse(root->left);
    }
    
    TreeNode* convertBST(TreeNode* root) {
        if(!root)    
            return root;
        
        curr_sum = 0;
        traverse(root);
        return root;
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
    def __init__(self):
        self.total = 0
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        self.convertBST(root.right)
        
        self.total += root.val
        root.val = self.total
        
        self.convertBST(root.left)
        
        return root
```
