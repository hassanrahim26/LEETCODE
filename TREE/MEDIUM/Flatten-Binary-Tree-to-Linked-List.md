## [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

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
    void flatten(TreeNode* root) {
        while(root)
        {
            if(root->left and root->right)
            {
                TreeNode* temp = root->left;
                while(temp->right)
                    temp = temp->right;
                temp->right = root->right;
            }
            
            if(root->left)
                root->right = root->left;
            root->left = NULL;
            root = root->right;
        }
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        while(root):
            if root.left and root.right:
                temp = root.left
                while temp.right:
                    temp = temp.right
                temp.right = root.right
            
            if root.left:
                root.right = root.left
            root.left = None
            root = root.right
```
