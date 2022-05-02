/*
PROBLEM LINK:- https://leetcode.com/problems/find-the-duplicate-number/
*/

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int low = 0, high = nums.size() - 1, c;
        
        while(low <= high){
            int mid = low + (high - low)/2;
            c = 0;
            
            for(int x: nums)
            {
                if(x <= mid)
                    c++;
            }
            
            if(c <= mid)
                low = mid + 1;
            else
                high = mid - 1;
        }
        
        return low;
    }
};
