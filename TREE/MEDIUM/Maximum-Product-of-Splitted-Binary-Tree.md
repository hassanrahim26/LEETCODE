## [Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/)

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
    long ans = 0, total = 0, s, mod = 1e9+7;
    int maxProduct(TreeNode* root) {
        total = solve(root), solve(root);
        return ans % mod;
    }
    int solve(TreeNode* root){
        if(!root) return 0;
        s = root->val + solve(root->left) + solve(root->right);
        ans = max(ans, s * (total - s));
        return s;
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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root: return 0
            s = root.val + solve(root.left) + solve(root.right)
            self.ans = max(self.ans, s * (self.total - s))
            return s
        self.ans = self.total = 0
        mod = 1e9+7
        self.total = solve(root)
        solve(root)
        return int(self.ans % mod)
```
