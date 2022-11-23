## [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

* **C++**

  * 1
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
      int countNodes(TreeNode* root) {
          if(root == NULL)
              return 0;
        
          int lh = 0, rh = 0;
          TreeNode *i = root, *j = root;
        
          while(i != NULL){
              i = i->left;
              lh++;
          }
        
          while(j != NULL){
              j = j->right;
              rh++;
          }
        
          if(lh == rh)
              return pow(2, lh) - 1;
        
          return 1+countNodes(root->left)+countNodes(root->right);
      }
  };
  ```
  
  * 2
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
      int countNodes(TreeNode* root) {
          if(root == NULL)    
              return 0;
        
          int ans = 1 + countNodes(root->left) + countNodes(root->right);
          return ans;
      }
  };
  ```
