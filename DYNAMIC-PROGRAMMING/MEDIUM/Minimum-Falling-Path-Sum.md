## [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/submissions/)

* **C++**
```cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& m) {
        int mx = INT_MAX, n = m.size();
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(j == 0 and j+1 < n and i)
                    m[i][j] += min({m[i-1][j+1], m[i-1][j]});
                if(j == n-1 and j-1 >= 0 and i)
                    m[i][j] += min({m[i-1][j-1], m[i-1][j]});
                if(j - 1 >= 0 and j+1 < n and i)
                    m[i][j] += min({m[i-1][j-1], m[i-1][j], m[i-1][j+1]});
                if(i == n-1)
                    mx = min(mx, m[i][j]);
            }
        }
        return mx;
    }
};
```
