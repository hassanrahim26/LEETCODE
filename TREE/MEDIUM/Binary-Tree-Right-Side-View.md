## [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

* **C++**
```cpp
class Solution {
public:
    int maxlevel = 0;
    
    void helper(TreeNode* root, vector<int>& ans, int currlevel)
    {
        if(root)    
        {
            if(currlevel > maxlevel)
            {
                ans.push_back(root->val);
                maxlevel = currlevel;               
            }
            
            helper(root->right, ans, currlevel + 1);
            helper(root->left, ans, currlevel + 1);
        }
    }
    
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        helper(root, ans, 1);
        return ans;
    }
};
```

