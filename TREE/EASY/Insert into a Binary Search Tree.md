## [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

* **C++**
```cpp
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        
        if(!root)
        {
            TreeNode* newNode = new TreeNode(val);
            return newNode;
        }
        
        if(root->val > val)
            root->left = insertIntoBST(root->left, val);
        else
            root->right = insertIntoBST(root->right, val);
        
        return root;
    }
};
```

* **Python**
```py
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            root = TreeNode(val)
            return root
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
```
