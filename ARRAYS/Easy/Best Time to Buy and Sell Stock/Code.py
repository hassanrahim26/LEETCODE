# PROBLEM LINK:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, m = 0, float('inf')
        for i in prices:
            m = min(m, i)
            x = i - m
            profit = max(profit, x)
        return profit
