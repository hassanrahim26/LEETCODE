/*
PROBLEM LINK:- https://leetcode.com/problems/richest-customer-wealth/
*/

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int wealth = INT_MIN;
        for(int i = 0; i < accounts.size(); i++)
        {
            int s = 0;
            for(int j = 0; j < accounts[i].size(); j++)
            {
                s += accounts[i][j];
            }
            wealth = max(wealth,s);
        }
        return wealth;
    }
};
