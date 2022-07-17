## [K Inverse Pairs Array](https://leetcode.com/problems/k-inverse-pairs-array/)

* **C++**
```cpp
class Solution {
public:
    int kInversePairs(int n, int k) {
        int dp[2][1001] = {1};
        for(int i = 1; i <= n; i++)
            for(int j = 0; j <= k; j++)
            {
                dp[i%2][j] = (dp[(i-1)%2][j] + (j > 0 ? dp[i%2][j-1] : 0)) % 1000000007;
                if(j >= i)
                    dp[i%2][j] = (1000000007 + dp[i%2][j] - dp[(i-1)%2][j-i]) % 1000000007;
            }
        return dp[n%2][k];
    }
};
```
