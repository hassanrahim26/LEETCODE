## [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

* **C++**
```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root == NULL)
            return 0;
        int l = minDepth(root -> left);
        int r = minDepth(root -> right);
        
        if(l == 0)
            return 1 + r;
        else if(r == 0)
            return 1 + l;
        return 1 + min(l, r);
    }
};

```

* **PYTHON**
```py
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if None in [root.left, root.right]:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```
