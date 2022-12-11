## [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

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
    int subTreeSum(TreeNode* root, int &mx){
        if(root == NULL) return 0;
        
        int l = max(0, subTreeSum(root->left, mx));
        int r = max(0, subTreeSum(root->right, mx));
        int csum = root->val+l+r;
        cout << csum << " ";
        
        mx = max(mx, csum);
        return root->val+max(l, r);
    }
    int maxPathSum(TreeNode* root) {
        int mx = INT_MIN;
        subTreeSum(root, mx);
        return mx;
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
    def maxPathSum(self, root: Optional[TreeNode], mx = -inf) -> int:
        def subTreeSum(root):
            nonlocal mx
            if not root: return 0
            
            l = max(0, subTreeSum(root.left))
            r = max(0, subTreeSum(root.right))
            csum = root.val + l + r
            
            mx = max(mx, csum)
            return root.val + max(l, r)
        subTreeSum(root)
        return mx
```
