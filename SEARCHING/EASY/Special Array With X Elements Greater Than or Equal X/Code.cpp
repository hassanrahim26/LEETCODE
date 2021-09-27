/*
PROBLEM LINK:- https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
*/

class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0, ans = 0; ans <= nums.size(); ++ans) {
            while (i < nums.size() && nums[i] < ans) ++i;
            if (ans == nums.size() - i) return ans;
        }
        return -1;
    }
};
