## [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/)

* **C++**
```cpp
class Solution {
public:
    int numTilings(int n) {
        unsigned int dp[n + 3]; dp[0] = 1; dp[1] = 2; dp[2] = 5;
        int mod = 1e9+7;
        for (int i = 3; i < n; i ++){
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod;
        }
        return dp[n - 1];
    }
};
```

* **PYTHON**
```py
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1e9+7
        dp = [1, 2, 5] + [0] * n
        for i in range(3, n):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % mod
        return int(dp[n - 1])
```
