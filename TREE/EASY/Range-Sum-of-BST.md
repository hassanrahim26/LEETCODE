## [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

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
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(!root) return 0;
        int s = (low <= root->val and root->val <= high) ? root->val : 0;
        if(low <= root->val)
            s += rangeSumBST(root->left, low, high);
        if(high >= root->val)
            s += rangeSumBST(root->right, low, high);
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        s = root.val if low <= root.val <= high else 0
        if(low <= root.val):
            s += self.rangeSumBST(root.left, low, high)
        if(high >= root.val):
            s += self.rangeSumBST(root.right, low, high)
        return s
```
