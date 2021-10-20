/*
PROBLEM LINK:- https://leetcode.com/problems/sum-of-unique-elements/
*/

class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        vector<int> v;
        for(auto x:nums)
            if(count(nums.begin(), nums.end(), x) == 1)
                v.push_back(x);
        return accumulate(v.begin(), v.end(), 0);
    }
};
