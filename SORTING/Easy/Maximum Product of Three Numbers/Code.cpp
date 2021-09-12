/*
PROBLEM LINK:- https://leetcode.com/problems/maximum-product-of-three-numbers/
*/

class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(),nums.end());
        int a = nums[n-1] * nums[n-2] * nums[n-3];
        int b = nums[0] * nums[1] * nums[n-1];
        return max(a,b);
    }
};
