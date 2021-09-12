/*
PROBLEM LINK:- https://leetcode.com/problems/missing-number/
*/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size(), m;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < n; i++)
        {
            if(i != nums[i])
            {
                m = i;
                break;
            }
        }
        return m;
    }
};
