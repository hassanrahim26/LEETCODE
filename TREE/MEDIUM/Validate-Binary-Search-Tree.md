## [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

* **C++**
  * **1**
    ```cpp
    class Solution {
    public:
      void inorder(TreeNode* root){
          if(!root)
             return;
          inorder(root->left);
          ans.push_back(root->val);
          inorder(root->right);
      }
    
      bool isValidBST(TreeNode* root) {
          if(!root)            
              return true;
        
          inorder(root);
          for(int i = 1; i < ans.size(); i++)
              if(ans[i] <= ans[i-1])
                  return false;
          return true;
      }
    
      private:
          vector<int> ans;
    };
    ```
  * **2**
    ```cpp
    class Solution {
    public:
      bool isValid(TreeNode* root, long min, long max) {
		      if(!root)
			        return true; 
		
          if(root->val > min && root->val < max)
			        return isValid(root->left, min, root->val) && isValid(root->right, root->val, max);
        
		      return false;
	    }
    
	    bool isValidBST(TreeNode* root) {
		      return isValid(root, LONG_MIN, LONG_MAX);
	    }
    };
    ```
