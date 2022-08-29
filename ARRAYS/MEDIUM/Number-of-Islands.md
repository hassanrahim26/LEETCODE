## [Number of Islands](https://leetcode.com/problems/number-of-islands/)

* **C++**
```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.size() == 0)    
            return 0;
        int c = 0;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == '1'){
                    c++;
                    solve(grid, i, j);
                }
            }
        }
        return c;
    }

    void solve(vector<vector<char>>& grid, int i, int j){
        int n = grid.size(), m = grid[0].size();
        if(i < 0 or i == n or j < 0 or j == m or grid[i][j] == '0')
            return;
        
        grid[i][j] = '0';
        solve(grid, i+1, j);
        solve(grid, i-1, j);
        solve(grid, i, j+1);
        solve(grid, i, j-1);
    }
};
```

* **PYTHON**
```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    c += 1
                    self.solve(grid, i, j)
        
        return c
    
    def solve(self, grid, i, j):
        n, m = len(grid), len(grid[0])
        if i < 0 or i == n or j < 0 or j == m or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        self.solve(grid, i+1, j)
        self.solve(grid, i-1, j)
        self.solve(grid, i, j+1)
        self.solve(grid, i, j-1)
```
