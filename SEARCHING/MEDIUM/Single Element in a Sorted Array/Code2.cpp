/*
PROBLEM LINK:- https://leetcode.com/problems/single-element-in-a-sorted-array/
*/

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        if(nums.size() == 0)
            return nums[0];
        
        int low = 0, high = nums.size() - 1, mid, x;
        
        while(low < high)
        {
            mid = low + (high - low)/2;
            x = (mid % 2 == 0) ? mid+1 : mid-1;
            
            if(nums[mid] == nums[x])
                low = mid + 1;
            else
                high = mid;
        }
        
        return nums[low];
    }
};
