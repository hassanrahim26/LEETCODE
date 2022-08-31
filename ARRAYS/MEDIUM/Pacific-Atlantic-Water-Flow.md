## [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>>ans;
        int n = heights.size();
        int m = heights[0].size();
        
        vector<vector<bool>> pacific(n, vector<bool>(m));
        vector<vector<bool>> atlantic(n, vector<bool>(m));
        
        for (int i = 0; i < n; i++){ 
            dfs(heights, pacific, i, 0);
            dfs(heights, atlantic, i, m-1);
        }
        
        for (int j = 0; j < m; j++){  
            dfs(heights, pacific, 0, j);
            dfs(heights, atlantic, n-1, j);
        }

        for (int i = 0; i < n; i++) 
            for (int j = 0; j < m; j++)    
                if (pacific[i][j] && atlantic[i][j]) 
                    ans.push_back({i,j});                 
        
        return ans;
    }
    
    void dfs(vector<vector<int>>& h, vector<vector<bool>>& vis, int i, int j) {   
        int n = h.size();
        int m = h[0].size();

        vis[i][j] = true;
        if (i-1 >= 0 && vis[i-1][j] != true && h[i-1][j] >= h[i][j])
            dfs(h, vis, i-1, j);
        if (i+1 < n && vis[i+1][j] != true && h[i+1][j] >= h[i][j])
            dfs(h, vis, i+1, j);
        if (j-1 >= 0 && vis[i][j-1] != true && h[i][j-1] >= h[i][j])
            dfs(h, vis, i, j-1);
        if (j+1 < m && vis[i][j+1] != true && h[i][j+1] >= h[i][j])
            dfs(h, vis, i, j+1);
    }
};
```
