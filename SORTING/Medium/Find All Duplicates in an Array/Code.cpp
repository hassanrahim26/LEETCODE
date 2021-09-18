/*
PROBLEM LINK:- https://leetcode.com/problems/find-all-duplicates-in-an-array/
*/

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int n = nums.size();
        vector<int> v;
        sort(nums.begin(), nums.end());
        for(int i = 1; i < n; i++)
        {
            if(nums[i-1] == nums[i])
            {
                v.push_back(nums[i]);
            }
        }
        return v;
    }
};
