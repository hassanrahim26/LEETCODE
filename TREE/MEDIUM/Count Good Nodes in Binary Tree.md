## [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

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
    int goodNodes(TreeNode* root, int val = INT_MIN) {
        int ans = 0;
        if(!root)
            return 0;
        if(root->val >= val){
            val = root->val;
            ans++;
        }
        ans += goodNodes(root->left, val) + goodNodes(root->right, val);
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
    def goodNodes(self, root: TreeNode, val = -100000) -> int:
        ans = 0
        if not root:
            return 0
        if root.val >= val:
            val = root.val
            ans += 1
        ans += self.goodNodes(root.left, val) + self.goodNodes(root.right, val)
        return ans
```
