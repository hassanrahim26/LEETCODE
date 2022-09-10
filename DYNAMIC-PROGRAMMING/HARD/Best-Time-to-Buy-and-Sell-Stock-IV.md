## [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

* **C++**
```cpp
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if(k == 0)  return 0;
        vector<vector<int>> dp(k+1, vector<int>(2));
        
        for(int i = 1; i <= k; i++)
            dp[i][0] = INT_MAX;
        
        for(auto &p: prices){
            for(int i = 1; i <= k; i++){
                dp[i][0] = min(dp[i][0], p - dp[i-1][1]);
                dp[i][1] = max(dp[i][1], p - dp[i][0]);
            }
        }
        return dp[k][1];
    }
};
```

* **PYTHON**
```py
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0: return 0
        dp = [[1000, 0] for _ in range(k + 1)]
              
        for p in prices:
            for i in range(1, k + 1):
                dp[i][0] = min(dp[i][0], p - dp[i-1][1])
                dp[i][1] = max(dp[i][1], p - dp[i][0])
        
        return dp[k][1]
```
