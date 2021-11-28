/*
PROBLEM LINK:- https://leetcode.com/problems/binary-tree-preorder-traversal/
*/

class Solution {
public:
    void preorder(TreeNode* root, vector<int>& v)
    {
        if(!root)
            return;
        
        v.push_back(root -> val);
        preorder(root -> left, v);
        preorder(root -> right, v);
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> v;
        preorder(root, v);
        return v;
    }
};
