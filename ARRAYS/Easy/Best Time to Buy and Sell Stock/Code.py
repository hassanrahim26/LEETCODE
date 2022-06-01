# PROBLEM LINK:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, ans, p = 10000, 0, 0

        for i in prices:
            if i < l:
                l = i
            p = i - l 
            if ans < p:
                ans = p 
                
        return ans
