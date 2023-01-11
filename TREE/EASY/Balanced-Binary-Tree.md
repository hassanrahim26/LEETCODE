## [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

* **C++**
```cpp
class Solution {
public:
    
    int height(TreeNode* root)
    {
        if(!root)
            return 0;
        
        int lh = height(root->left);
        int rh = height(root->right);
        
        return 1 + max(lh, rh);
    }
    
    bool isBalanced(TreeNode* root) {
        if(!root)        
            return true;
        
        bool ans = true;
        int lh = height(root->left);
        int rh = height(root->right);
        
        if((abs(lh-rh) <= 1) && isBalanced(root->left) && isBalanced(root->right))
            return true;
        
        return false;
    }
};
```

* **PYTHON**
```py
class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        return 1 + max(lh, rh)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        if (abs(lh - rh) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False
```
