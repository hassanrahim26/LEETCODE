## [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

* **C++**
```cpp
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(root)    
        {
            if(root->val > key)
                root->left = deleteNode(root->left, key);
            else if(root->val < key)
                root->right = deleteNode(root->right, key);
            else
            {
                if(!root->left && !root->right)
                    return NULL;
                if(!root->left || !root->right)
                    return root->left ? root->left : root->right;
                
                TreeNode *temp = root->left;
                while(temp->right != NULL)
                {
                    temp = temp->right;
                }
                
                root->val = temp->val;
                root->left = deleteNode(root->left, temp->val);
            }   
        }
        
        return root;
     }
};
```

* **Python**
```py
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                if not root.left and not root.right:
                    return None
                if not root.left or not root.right:
                    return root.left if root.left else root.right
                
                temp = root.left
                while(temp.right != None):
                    temp = temp.right
                
                root.val = temp.val
                root.left = self.deleteNode(root.left, temp.val)
        return root
```
