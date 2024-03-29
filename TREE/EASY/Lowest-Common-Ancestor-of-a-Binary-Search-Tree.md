## [Lowest Common Ancestor of a Binary Search Tre](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

* **C++**
  * **1**
    ```cpp
    /**
    * Definition for a binary tree node.
    * struct TreeNode {
    *     int val;
    *     TreeNode *left;
    *     TreeNode *right;
    *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    * };
    */

    class Solution {
    public:
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            if((root->val > p->val) and (root->val > q->val))
                 return lowestCommonAncestor(root->left, p, q);
        
            if((root->val < p->val) and (root->val < q->val))
                 return lowestCommonAncestor(root->right, p, q);
           
            return root;
        }
    };
    ```
  * **2** 
    ```cpp
    /**
    * Definition for a binary tree node.
     * struct TreeNode {
     *     int val;
     *     TreeNode *left;
     *     TreeNode *right;
     *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
     * };
     */

    class Solution {
    public:
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            if(root == p or root == q or !root)
                return root;
        
            TreeNode *left = lowestCommonAncestor(root->left, p, q);
            TreeNode *right = lowestCommonAncestor(root->right, p, q);
        
            if(left and right)
                return root;    
            else if(left)
                return left;

            return right;
        }
    };
    ```

* **Python**
  * **1**
    ```py
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution:
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            if root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right, p, q)
            return root
    ```
  * **2**
    ```py
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution:
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if(root == p or root == q or not root):
                return root
        
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
        
            if left and right:  return root
            elif left:  return left
            return right
    ```
