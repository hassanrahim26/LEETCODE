/*
PROBLEM LINK:- https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
*/

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> v;
        for(int i = 0; i < nums.size(); i++)
        {
            int x = abs(nums[i]) - 1;
            if(nums[x] > 0) nums[x] = -nums[x];
        }
        
        for(int i = 0; i < nums.size(); i++)
        {
            if(nums[i] > 0)
                v.push_back(i+1);
        }
        return v;
    }
};
