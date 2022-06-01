/*
PROBLEM LINK:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = INT_MAX, ans = 0, p = 0;
        
        for(int x: prices){
            if(x < l)
                l = x;
            p = x - l;
            
            if(ans < p)
                ans = p;
        }
        
        return ans;
    }
};
