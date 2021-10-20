/*
PROBLEM LINK:- https://leetcode.com/problems/sum-of-unique-elements/
*/

class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        int s = 0;
        unordered_map<int, int> mp;
        
        for(auto x:nums)
            mp[x]++;
        
        for(auto m:mp)
            if(m.second == 1)
                s += m.first;
        
        return s;    
    }
};
