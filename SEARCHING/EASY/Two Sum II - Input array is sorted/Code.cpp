/*
PROBLEM LINK:- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1, sum;
        vector<int> v;
        while(start < end)
        {
            sum = nums[start] + nums[end];
            if(sum < target)
            {
                start++;
            }
            else if(sum > target)
            {
                end--;
            }
            else
            {
                v.push_back(start+1);
                v.push_back(end+1);
                break;
            }
        }
        return v;
    }
};
