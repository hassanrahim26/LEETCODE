/*
PROBLEM LINK:- https://leetcode.com/problems/shuffle-the-array/
*/

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        int m = nums.size();
        vector<int> v(m);
        for(int i = 0, j = 0; i < n; i++, j+= 2)
        {
            v[j] = nums[i];
            v[j+1] = nums[i+n];
        }
        return v;
    }
};
