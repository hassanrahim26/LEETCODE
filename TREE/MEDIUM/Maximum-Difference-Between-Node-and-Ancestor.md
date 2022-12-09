## [Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/)

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
    int maxAncestorDiff(TreeNode* root, int mn = INT_MAX, int mx = INT_MIN) {
        if(!root) return mx - mn;
        mn = min(mn, root->val);
        mx = max(mx, root->val);
        return max(maxAncestorDiff(root->left, mn, mx), maxAncestorDiff(root->right, mn, mx));
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
    def maxAncestorDiff(self, root, mn = inf, mx = -inf):
        if not root: return mx - mn
        mn, mx = min(mn, root.val), max(mx, root.val)
        return max(self.maxAncestorDiff(root.left, mn, mx), self.maxAncestorDiff(root.right, mn, mx))
```
