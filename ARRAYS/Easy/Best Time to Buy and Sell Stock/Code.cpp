/*
PROBLEM LINK:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0, x = INT_MAX;
        for(int i = 0; i < prices.size(); i++)
        {
            x = min(x, prices[i]);
            if(x < prices[i])
                profit = max(profit, (prices[i] - x));
        }
        return profit;
    }
};
