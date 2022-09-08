## [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

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
        void inorder(TreeNode* root, vector<int>& v){
            if(!root)    
                return;
            inorder(root->left, v);
            v.push_back(root->val);
            inorder(root->right, v);
        }
        
        vector<int> inorderTraversal(TreeNode* root) {
            vector<int> v;    
            inorder(root, v);
            return v;
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
        vector<int> inorderTraversal(TreeNode* root) {
            if(!root)
                return {};
            inorderTraversal(root->left);
            v.push_back(root->val);
            inorderTraversal(root->right);
            return v;
        }
    };
    ```
<hr>

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
        def inorder(self, root, v):
            if not root:
                return
        
            self.inorder(root.left, v)
            v.append(root.val)
            self.inorder(root.right, v)
            
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            v = []
            self.inorder(root, v)
            return v
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
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []  
    ```
