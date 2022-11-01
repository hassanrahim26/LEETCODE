## [Where Will the Ball Fall](https://leetcode.com/problems/where-will-the-ball-fall/)

* **C++**
```cpp
class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> ans;
        
        for(int col = 0; col < n; col++)
        {
            int cur_col = col;
            for(int cur_row = 0; cur_row < m; cur_row++)
            {
                int next_col = cur_col + grid[cur_row][cur_col];
                if(next_col < 0 || next_col >= n || grid[cur_row][cur_col] ^ grid[cur_row][next_col])
                {
                    cur_col = -1;
                    break;
                }
                cur_col = next_col;
            }
            ans.push_back(cur_col);
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        
        for col in range(n):
            cur_col = col
            for cur_row in range(m):
                next_col = cur_col + grid[cur_row][cur_col]
                if(next_col < 0 or next_col >= n or grid[cur_row][cur_col] ^ grid[cur_row][next_col]):
                    cur_col = -1
                    break
                cur_col = next_col
            ans.append(cur_col)
        return ans
```
