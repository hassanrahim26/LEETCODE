## [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<int>> ans;    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& g) {
        vector<int> path;
        dfs(g, 0, path);
        return ans;
    }
    void dfs(vector<vector<int>>& g, int i, vector<int>& path){
        path.push_back(i);
        if(i == g.size() - 1){
            ans.push_back(path);
        }
        else{
            for(auto child: g[i])
                dfs(g, child, path);
        }
        path.pop_back();
    }
};
```

* **PYTHON**
```py
class Solution:
    def allPathsSourceTarget(self, g):
        ans = []
        def dfs(path):
            if path[-1] == len(g)-1: ans.append(path)
            else:
                for child in g[path[-1]]:
                    dfs(path + [child])
        dfs([0])
        return ans
```
