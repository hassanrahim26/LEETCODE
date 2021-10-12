/*
PROBLEM LINK:- https://leetcode.com/problems/median-of-two-sorted-arrays/
*/

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<double> v;
        
        for(int i = 0; i < nums1.size(); i++)
        {
            v.push_back(nums1[i]);
        }
        
        for(int i = 0; i < nums2.size(); i++)
        {
            v.push_back(nums2[i]);
        }
        
        sort(v.begin(), v.end());
        
        int x = v.size();
        
        if(x % 2 == 0)
        {
            return (v[(x/2) - 1] + v[x/2])/2;
        }
        
        return v[x/2];
    }
};
