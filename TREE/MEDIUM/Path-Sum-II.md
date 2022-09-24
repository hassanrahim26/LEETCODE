## [Path Sum II](https://leetcode.com/problems/path-sum-ii/)

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
    vector<vector<int>> ans;
    
    void dfs(TreeNode* node, vector<int>& path, int s){
        if(!node)   return;
        path.push_back(node->val);
        
        if(!node->left and !node->right and s == node->val)
            ans.push_back(path);
        dfs(node->left, path, s - node->val);
        dfs(node->right, path, s - node->val);
        path.pop_back();
    }
    vector<vector<int>> pathSum(TreeNode* root, int s) {
        vector<int> path;
        dfs(root, path, s);
        return ans;
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
    def dfs(self, root, path, ans, s):
        if not root:
            return
        path.append(root.val)
        
        if not root.left and not root.right and s == root.val:
            ans.append(list(path))
        
        self.dfs(root.left, path, ans, s - root.val)
        self.dfs(root.right, path, ans, s - root.val)
        path.pop()
        
    def pathSum(self, root: Optional[TreeNode], s: int) -> List[List[int]]:
        ans = []
        self.dfs(root, [], ans, s)
        return ans
```
