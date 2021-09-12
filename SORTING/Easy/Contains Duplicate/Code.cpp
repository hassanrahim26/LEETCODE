/*
PROBLEM LINK:- https://leetcode.com/problems/contains-duplicate/
*/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for(int i = 1; i < n; i++)
            if(nums[i-1] == nums[i])
                return true;
        return false;
    }
};
