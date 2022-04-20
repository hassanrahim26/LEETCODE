## [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

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
    TreeNode* first, *last, *prev;
public:
    void inorder(TreeNode* root){
        if(root == NULL)
            return;
        inorder(root->left);
        
        if(prev != NULL && (root->val < prev->val))
        {
            if(first == NULL)    
            {
                first = prev;
                last = root;
            }
            else
                last = root;
        }
        
        prev = root;
        inorder(root->right);
    }
    
    void recoverTree(TreeNode* root) {
        first = last = prev = NULL;
        inorder(root);
        
        int temp = first->val;
        first->val = last->val;
        last->val = temp;
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            
            if self.prev and self.prev.val > root.val:
                if self.first == None:
                    self.first = self.prev
                    self.last = root
                else:
                    self.last = root
                    
            self.prev = root
            inorder(root.right)
        
        self.first = self.last = self.prev = None
        inorder(root)
        self.first.val, self.last.val = self.last.val, self.first.val
```
