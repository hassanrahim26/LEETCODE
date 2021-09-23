/*
PROBLEM LINK:- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
*/

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
    int a = BinarySearch(nums, target);
    int b = BinarySearch(nums, target+1)-1;
    if (a < nums.size() && nums[a] == target)
        return {a, b};
    else
        return {-1, -1};
    }

    int BinarySearch(vector<int>& nums, int target) 
    {
        int low = 0, high = nums.size()-1;
        while (low <= high) 
        {
            int mid = low + (high - low)/2;
            if (nums[mid] < target)
                low = mid+1;
            else
                high = mid-1;
        }
        return low;
    }
};
