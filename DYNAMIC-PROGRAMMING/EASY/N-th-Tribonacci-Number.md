## [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)

* **C++**
```cpp
class Solution {
public:
    int tribonacci(int n) {
        int dp[3] = {0, 1, 1};
        for(int i = 3; i <= n; i++){
            dp[i % 3] += dp[(i + 1) % 3] + dp[(i + 2) % 3];
        }
        return dp[n % 3];
    }
};
```

* **Python**
```py
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n+1):
            dp[i % 3] += dp[(i + 1) % 3] + dp[(i + 2) % 3]
        return dp[n % 3]
```
