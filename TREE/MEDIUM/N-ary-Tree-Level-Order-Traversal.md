## [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

* **C++**
```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ans;
        if(root == NULL)    return ans;
        
        queue<Node*> q;
        q.push(root);
        
        while(!q.empty()){
            vector<int> temp;
            int n = q.size();
            
            for(int i = 0; i < n; i++){
                temp.push_back(q.front()->val);
                Node *temp = q.front();
                q.pop();
                
                for(Node *child: temp->children)
                    q.push(child);
            }
            ans.push_back(temp);
        }
        return ans;
    }
};
```

* **PYTHON**
```py
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        q, ans = [root], []
        while any(q):
            ans.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ans
```
