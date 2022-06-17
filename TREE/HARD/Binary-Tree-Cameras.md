## [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)

* **C++**
```cpp
class Solution {
public:
    int ans = 0;
    int dfs(TreeNode *root){
        if(!root)
            return 0;
        
        int val = dfs(root->left) + dfs(root->right);
        if(val == 0)
            return 3;
        if(val < 3)
            return 0;
        ans++;
        return 1;
    }
    
    int minCameraCover(TreeNode* root) {
        return dfs(root) > 2 ? ans + 1 : ans;
    }
};
```

* **Python**
```py
class Solution:
    ans = 0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            
            val = dfs(root.left) + dfs(root.right)
            
            if val == 0:
                return 3
            if val < 3:
                return 0
        
            self.ans += 1
            return 1
        
        return self.ans + 1 if dfs(root) > 2 else self.ans
```
