## [Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

* **C++**
```cpp
class Solution {
public:
    int dfs(vector<vector<int>>& grid, int i, int j){
        if(i >= 0 and i < grid.size() and j >= 0 and j < grid[0].size() and grid[i][j] == 1){
            grid[i][j] = 0;
            return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1);
        }
        return 0;
    }
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0;
        for(int i = 0; i < grid.size(); i++)
            for(int j = 0; j < grid[0].size(); j++)
                if(grid[i][j] == 1)
                    max_area = max(max_area, dfs(grid, i, j));
        return max_area;
    }
};
```

* **Python**
```py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        def dfs(grid, i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1) 
        
            return 0
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(grid, i, j))
        
        return max_area
```
