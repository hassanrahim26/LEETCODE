/*
PROBLEM LINK:- https://leetcode.com/problems/third-maximum-number/
*/

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        vector<int> v;
        
        for(int x : s)
        {
            v.push_back(x);
        }
        
        int n = v.size();
        
        if(n<3)
            return v[n-1];
        return v[n-3];
    }
};
