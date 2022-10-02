## [Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)

* **C++**
```cpp
class Solution {
public:
    int numRollsToTarget(int n, int f, int target) {
        vector<vector<int> > dp(n+1, vector<int>(target+1, 0));
        // dp(i, j) means the number of ways to reach target "j" using exactly "i" dice. 
        int mod = 1000000007;
        dp[0][0] = 1;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= target; j++){
                for(int k = 1; k <= f; k++){
                   if(k <= j)
                       dp[i][j] = ((dp[i][j] % mod) + dp[i-1][j-k] % mod) % mod;
                }
            }
        }
        return dp[n][target];
    }
};
```

* **PYTHON**
```py
class Solution:
    def numRollsToTarget(self, n: int, f: int, target: int) -> int:
        dp = [[0 for i in range(target+1)] for j in range(n+1)]
        dp[0][0] = 1
        mod = 10**9+7
        for i in range(1, n+1):
            for j in range(1, target+1):
                for k in range(1, f+1):
                    if(k <= j):
                        dp[i][j] = ((dp[i][j] % mod) + dp[i-1][j-k] % mod) % mod
        
        return dp[n][target]
```
