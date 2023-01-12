## [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

* **C++**
```cpp
class Solution {
public:
    void postorder(TreeNode* root, vector<int>& v)
    {
        if(!root)
            return;
        
        postorder(root -> left, v);
        postorder(root -> right, v);
        v.push_back(root -> val);
    }
    
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> v;
        postorder(root, v);
        return v;
    }
};
```

* **PYTHON**
```py
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
```
