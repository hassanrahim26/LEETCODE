/*
PROBLEM LINK:- https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
*/

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int n = nums.size();
        vector<int> v;
        for(int i = 0; i < n; i++)
        {
            int c = 0;
            int x = nums[i];
            for(int j = 0; j < n; j++)
            {
                if(i != j and x > nums[j])
                {
                    c++;
                }
            }
            v.push_back(c);
        }
        return v;
    }
};
