## [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

* **C++**

  * 1
  ```cpp
  /**
   * Definition for a binary tree node.
  *  struct TreeNode {
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
      void solve(TreeNode* root, vector<int>& ans){
          if(!root)   
              return;
            
          ans.push_back(root->val);
          solve(root->left, ans);
          solve(root->right, ans);
      }
    
      vector<int> preorderTraversal(TreeNode* root) {
          vector<int> ans;
          solve(root, ans);
          return ans;
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
      vector<int> ans;
      vector<int> preorderTraversal(TreeNode* root) {
          if(root){
              ans.push_back(root->val);
              preorderTraversal(root->left);
              preorderTraversal(root->right);
          }
          return ans;
      }
  };
  ```

<hr>

* **PYTHON**
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, v):
        if not root:
            return
        
        v.append(root.val)
        self.preorder(root.left, v)
        self.preorder(root.right, v)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        v = []
        self.preorder(root, v)
        return v
```
