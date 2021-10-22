/*
PROBLEM LINK:- https://leetcode.com/problems/search-insert-position/
*/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        while(start <= end)
        {
            int mid = start + (end-start)/2;
            if(target > nums[mid])
                start = mid + 1;
            else
                end = mid - 1;
        }
        return start;
    }
};
