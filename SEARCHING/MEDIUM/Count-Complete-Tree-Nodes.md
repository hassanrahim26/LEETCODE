## [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

* **C++**
```cpp
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

* **Python**
```py
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lh, rh = 0, 0
        i, j = root, root
        
        while i != None:
            i = i.left
            lh += 1
        
        while j != None:
            j = j.right
            rh += 1
        
        if lh == rh:
            return pow(2, lh) - 1
    
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```
