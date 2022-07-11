## [Unique Paths](https://leetcode.com/problems/unique-paths/)

* **C++**
```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++)
                dp[j] += dp[j-1];
        return dp[n-1];
    }
};
```

* **Python**
```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for _, j in product(range(1, m), range(1, n)):
            dp[j] += dp[j-1]
        return dp[n-1]
```
