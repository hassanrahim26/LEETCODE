## [Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)

* **C++**
```cpp
class Solution {
public:
    int minDifficulty(vector<int>& v, int d) {
        int n = v.size(), inf = 1e9, m;
        if(n < d){
            return -1;
        }
        vector<int> dp(n+1, 1e9);
        dp[n] = 0;
        for(int k = 1; k <= d; k++){
            for(int i = 0; i <= n-k; i++){
                m = 0, dp[i] = inf;
                for(int j = i; j <= n-k; j++){
                    m = max(m, v[j]);
                    dp[i] = min(dp[i], m + dp[j+1]);
                }
            }
        }
        return dp[0];
    }
};
```
