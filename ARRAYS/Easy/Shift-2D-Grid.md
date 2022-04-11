## [Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int n = grid.size();
        int m = grid[0].size();
        
        vector<vector<int>> ans(n, vector<int>(m));
        
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                int newI = (i+(j+k)/m)%n;
                int newJ = (j+k)%m;
                ans[newI][newJ] = grid[i][j];
            }
        }
        
        return ans;
    }
};
```
