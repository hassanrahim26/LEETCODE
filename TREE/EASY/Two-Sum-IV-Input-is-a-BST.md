## [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

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
  *      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  *    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  * };
  */
  class Solution {  
  public:
      unordered_set<int> s;
      bool findTarget(TreeNode* root, int k) {
          if(!root)   return false;
          if(s.count(k - root->val))  return true;
          s.insert(root->val);
          return findTarget(root->left, k) || findTarget(root->right, k);
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
       vector<int> v;
       void inorder(TreeNode* root){
           if(!root)
               return;
           inorder(root->left);
           v.push_back(root->val);
           inorder(root->right);
       }
     
       bool findTarget(TreeNode* root, int k) {
           inorder(root);
           int l = 0, r = v.size()-1;
           while(l < r){
               if(v[l] + v[r] == k)
                   return true;
               else{
                   if(v[l] + v[r] < k)
                       l++;
                   else
                       r--;
               }
           }
           return false;
       }
   };
   ```
   
* **PYTHON**
  * 1
  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
          def dfs(root, s):
              if root == None: 
                  return False
              x = k - root.val
              if x in s: 
                  return True
            
              s.add(root.val)
              return dfs(root.left, s) or dfs(root.right, s)
          return dfs(root, set())
  ```
  
  * 2
  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def inorder(self, root, v):
          if not root:
              return
          self.inorder(root.left, v)
          v.append(root.val)
          self.inorder(root.right, v)
          return v
        
      def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
          v = []
          self.inorder(root, v)
          l, r = 0, len(v)-1
          while(l < r):
              if(v[l] + v[r] == k):
                  return True
              else:
                  if(v[l] + v[r] < k):
                      l += 1
                  else:
                      r -= 1
          return False
  ```
