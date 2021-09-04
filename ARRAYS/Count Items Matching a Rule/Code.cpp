/*
PROBLEM LINK:- https://leetcode.com/problems/count-items-matching-a-rule/
*/

class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int n = items.size();
        int x, c = 0;
        
        if(ruleKey == "type") x = 0;
        if(ruleKey == "color") x = 1;
        if(ruleKey == "name") x = 2;
        
        for(int i = 0; i < n; i++)
        {
            if(items[i][x] == ruleValue)
                c++;
        }
        
        return c;
    }
};
