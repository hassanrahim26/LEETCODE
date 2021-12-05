/*
PROBLEM LINK:- https://leetcode.com/problems/sum-of-left-leaves/
*/

class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if(!root)
            return 0;
        
        if(root -> left && !root -> left -> left && !root -> left -> right)
            return root -> left -> val + sumOfLeftLeaves(root -> right);
        
        return sumOfLeftLeaves(root -> left) + sumOfLeftLeaves(root -> right);
    }
};
