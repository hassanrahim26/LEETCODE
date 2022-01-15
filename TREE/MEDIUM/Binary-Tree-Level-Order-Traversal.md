## [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root)
            return {};
        
        vector<vector<int>> ans;  
        
        queue<TreeNode*> q;
        q.push(root);
        
        TreeNode *temp;
        int len;
        
        while(!q.empty())
        {
            len = q.size();
            vector<int> v;
            
            for(int i = 0; i < len; i++)
            {
                temp = q.front();
                q.pop();
                v.push_back(temp->val);
                
                if(temp->left)  
                    q.push(temp->left);
                if(temp->right)
                    q.push(temp->right);
            }
            
            ans.push_back(v);
        }
        
        return ans;
    }
};
```
* **Python**
```py
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = [root]
        
        while queue:
            v = []
            
            for i in range(len(queue)):
                temp = queue.pop(0)
                v.append(temp.val)
                
                if temp.left:
                    queue.append(temp.left)
                
                if temp.right:
                    queue.append(temp.right)
                
            ans.append(v)
        
        return ans
                
```
