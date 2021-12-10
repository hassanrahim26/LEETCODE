/*
PROBLEM LINK:- https://leetcode.com/problems/single-element-in-a-sorted-array/
*/

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int x = 0, i = 0;
        while(i != nums.size())
        {
            x ^= nums[i];
            i++;
        }
        
        return x;
    }
};
