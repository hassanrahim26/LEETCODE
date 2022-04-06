## [N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

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
private:
    void solve(Node* root, vector<int>& ans) {
        if (root == nullptr) {
            return;
        }
        
        ans.push_back(root -> val);
        for (Node* child : root -> children) {
            solve(child, ans);
        }
    }
    
public:
    vector<int> preorder(Node* root) {
        vector<int> ans;
        solve(root, ans);
        return ans;
    }
};
```

* **Python**
```py
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node', ans: list = None) -> List[int]:
        if not root:
            return ans
        
        if ans == None:
            ans = []
        
        ans.append(root.val)
        
        for child in root.children:
            self.preorder(child, ans)
        
        return ans
```
