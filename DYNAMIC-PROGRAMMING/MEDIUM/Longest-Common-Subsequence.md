## [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

* **C++**
```cpp
class Solution {
public:
    int dp[1001][1001];
    int longestCommonSubsequence(string t1, string t2) {
        int n1 = t1.size(), n2 = t2.size();
        
        for(int i = 0; i <= n1; i++)
            dp[i][0] = 0;
        for(int i = 0; i <= n2; i++)
            dp[0][i] = 0;
        
        for(int i = 1; i <= n1; i++){
            for(int j = 1; j <= n2; j++){
                if(t1[i-1] == t2[j-1])
                    dp[i][j] = 1 + dp[i-1][j-1];
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[n1][n2];
    }
};
```

* **PYTHON**
```py
class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        dp = [[0]*(1001) for _ in range(1001)]
        n1, n2 = len(t1), len(t2)
            
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if(t1[i-1] == t2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n1][n2]
```
