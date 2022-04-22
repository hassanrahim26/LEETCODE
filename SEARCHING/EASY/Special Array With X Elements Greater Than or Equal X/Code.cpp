/*
PROBLEM LINK:- https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
*/

class Solution {
public:
    int specialArray(vector<int>& nums) {
        int low = 0, high = nums.size() - 1, mid, x;
        sort(nums.begin(), nums.end());
        while(low <= high){
            mid = low + (high - low)/2;
            x = nums.size() - mid;
            
            if(nums[mid] >= x)
                if(mid == 0 or nums[mid - 1] < x)
                    return x;
                else
                    high = mid - 1;
            else
                low = mid + 1;
        }
        
        return -1;
    }
};
