## [Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/)

* **C++**
```cpp
class Solution {
public:
    int dp[55][55][55];
    long long mod = 1e9 + 7;
    int dfs(int i, int j, int n, int m, int x){
        
        if(i < 0 || i >= n || j < 0 || j >= m)
            return 1;
        if(x <= 0)
            return 0;
        if(dp[i][j][x] != -1)
            return dp[i][j][x];
        
        int a = dfs(i-1,j,n,m,x-1);
        int b = dfs(i+1,j,n,m,x-1);
        int c = dfs(i,j-1,n,m,x-1);
        int d = dfs(i,j+1,n,m,x-1);
        int total = (a % mod + b % mod + c % mod + d % mod) % mod;
        dp[i][j][x] = total;
        return dp[i][j][x];
    }
    
    int findPaths(int n, int m, int maxMove, int row, int column) {
        memset(dp, -1, sizeof(dp));
        return dfs(row,column,n,m,maxMove);
    }
};
```
