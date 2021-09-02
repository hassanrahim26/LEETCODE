/*
PROBLEM LINK:- https://leetcode.com/problems/maximum-subarray/
*/

class Solution {
public:
    int maxSubArray(vector<int>& v) {
        int n = v.size();
        int m1 = v[0], m2 = v[0];
        for(int i = 1; i < n; i++)
        {
            m1 = max(v[i],v[i]+m1);
            m2 = max(m1,m2);
        }
        return m2;
    }
};
