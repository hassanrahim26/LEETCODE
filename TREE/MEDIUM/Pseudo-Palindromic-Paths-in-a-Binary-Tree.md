## [Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/)

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
    int pseudoPalindromicPaths (TreeNode* root, int count = 0) {
        if(!root) return 0;
        count ^= 1 << (root->val - 1);
        int ans = pseudoPalindromicPaths(root->left, count) + pseudoPalindromicPaths(root->right, count);
        if(root->left == root->right and (count & (count - 1)) == 0)
            ans++;
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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode], count = 0) -> int:
        if not root: return 0
        count ^= 1 << (root.val - 1)
        ans = self.pseudoPalindromicPaths(root.left, count) + self.pseudoPalindromicPaths(root.right, count)
        if((root.left == root.right) and (count & (count - 1) == 0)):
            ans += 1
        return ans
```
