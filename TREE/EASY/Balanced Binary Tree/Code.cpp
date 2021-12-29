/*
PROBLEM LINK:- https://leetcode.com/problems/balanced-binary-tree/
*/

class Solution {
public:
    
    int height(TreeNode* root)
    {
        if(!root)
            return 0;
        
        int lh = height(root->left);
        int rh = height(root->right);
        
        return 1 + max(lh, rh);
    }
    
    bool isBalanced(TreeNode* root) {
        if(!root)        
            return true;
        
        bool ans = true;
        int lh = height(root->left);
        int rh = height(root->right);
        
        if((abs(lh-rh) <= 1) && isBalanced(root->left) && isBalanced(root->right))
            return true;
        
        return false;
    }
};
