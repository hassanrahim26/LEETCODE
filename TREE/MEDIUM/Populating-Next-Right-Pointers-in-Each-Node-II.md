## [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

* **C++**
```cpp
class Solution {
public:
    Node* connect(Node* root) {
        if(root == NULL)    
            return NULL;
        
        queue<Node*> q;
        q.push(root);
        
        while(!q.empty()){
            int n = q.size();
            
            for(int i = 0; i < n; i++){
                Node *item = q.front();
                
                if(n - 1 == 1)
                    item->next = NULL;
                
                q.pop();
                
                if(n - 1 != i)
                    item->next = q.front();
                
                if(item -> left != NULL)
                    q.push(item -> left);
                if(item -> right != NULL)
                    q.push(item -> right);
            }
        }
        return root;   
    }
};
```
