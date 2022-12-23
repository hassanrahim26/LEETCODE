## [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

* **C++**
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = INT_MIN, sell = 0, prev_sell = 0, prev_buy = 0;
        
        for(auto i: prices){
            prev_buy = buy;
            buy = max(prev_sell - i, buy);
            prev_sell = sell;
            sell = max(prev_buy + i, sell);
        }
        
        return sell;
    }
};
```

* **Python**
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        
        for i in prices:
            prev_buy = buy
            buy = max(prev_sell - i, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + i, prev_sell)
        
        return sell
```
