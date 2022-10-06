## [Add One Row to Tree](https://leetcode.com/problems/add-one-row-to-tree/)

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
    TreeNode* solve(TreeNode* root, int v, int d, string dir) {
        if(d == 1){
            TreeNode *node = new TreeNode(v);
            if(dir == "left")   node->left = root;
            if(dir == "right")   node->right = root;
            return node;
        }
        if(root == nullptr) return root;
        root->left = solve(root->left, v, d-1, "left");
        root->right = solve(root->right, v, d-1, "right");
        return root;
    }
    TreeNode* addOneRow(TreeNode* root, int v, int d){
        return solve(root, v, d, "left");
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
    def solve(self, root, v, d, dir):
        if(d == 1):
            node = TreeNode(v)
            if(dir == "left"):  node.left = root
            if(dir == "right"): node.right = root
            return node
        
        if(root == None):
            return root
        root.left = self.solve(root.left, v, d-1, "left")
        root.right = self.solve(root.right, v, d-1, "right")
        return root
    
    def addOneRow(self, root: Optional[TreeNode], v: int, d: int) -> Optional[TreeNode]:
        return self.solve(root, v, d, "left")
```
