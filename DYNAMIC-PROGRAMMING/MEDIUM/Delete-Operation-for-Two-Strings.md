## [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

* **C++**
```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m= word1.length(), n = word2.length();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        
        for(int i = 0; i <= m; i++){
            for(int j = 0; j <= n; j++){
                if(i == 0 || j == 0)
                    continue;
                else if(word1[i-1] == word2[j-1])
                    dp[i][j] = 1 + dp[i-1][j-1];
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return m + n - 2 * dp[m][n];
    }
};
```

* **Python**
```py
def minDistance(self, w1, w2):
        m, n = len(w1), len(w2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (w1[i] == w2[j]))
        return m + n - 2 * dp[m][n]
```
