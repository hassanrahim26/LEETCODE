## [Lowest Common Ancestor of a Binary Search Tre](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

* **C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if((root->val > p->val) and (root->val > q->val))
            return lowestCommonAncestor(root->left, p, q);
        
        if((root->val < p->val) and (root->val < q->val))
           return lowestCommonAncestor(root->right, p, q);
           
        return root;
    }
};
```
