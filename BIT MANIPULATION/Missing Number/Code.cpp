/*
PROBLEM LINK:- https://leetcode.com/problems/missing-number/
*/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size(), i = 0;
        for(int x: nums)
        {
            n ^= x;
            n ^= i;
            i++;
        }
        
        return n;
    }
};
