## [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)

* **C++**
```cpp
class Solution {
public:
    int ans = 0, empty = 1;
    void dfs(vector<vector<int>>& grid, int x, int y, int count) {
        if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size() || grid[x][y] == -1) return;
        
        if (grid[x][y] == 2) {
            if(empty == count) ans++; 
            return;
        }
        
        grid[x][y] = -1;
        
        dfs(grid, x+1, y, count+1);
        dfs(grid, x-1, y, count+1);
        dfs(grid, x, y+1, count+1);
        dfs(grid, x, y-1, count+1);
        
        grid[x][y] = 0;
        
    }
    
    int uniquePathsIII(vector<vector<int>>& grid) {
        int x, y;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) x = i, y = j;
                else if (grid[i][j] == 0) empty++;
            }
        }
        
        dfs(grid, x, y, 0);
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans, self.empty = 0, 1
        def dfs(grid, x, y, count):
            if(x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == -1):
                return
            if(grid[x][y] == 2):
                if(self.empty == count): self.ans += 1
                return
            
            grid[x][y] = -1
            
            dfs(grid, x+1, y, count+1)
            dfs(grid, x-1, y, count+1)
            dfs(grid, x, y+1, count+1)
            dfs(grid, x, y-1, count+1)
            
            grid[x][y] = 1
            
        x, y = 0, 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    x, y = i, j
                elif(grid[i][j] == 0):
                    self.empty += 1
        dfs(grid, x, y, 0)
        return self.ans
```
