## [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)

* **C++**
```cpp
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root == NULL)    
            return 0;
        if(root->val == val)
            return root;
        if(root->val > val)
            return searchBST(root->left, val);
        return searchBST(root->right, val);
    }
};
```

* **Python**
```py
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        
        return self.searchBST(root.right, val)
```
