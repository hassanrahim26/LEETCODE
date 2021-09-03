/*
PROBLEM LINK:- https://leetcode.com/problems/find-the-highest-altitude/
*/

class Solution {
public:
    int largestAltitude(vector<int>& x) {
        int n = x.size();
        vector<int> v(n+1);
        v[0] = 0;
        for(int i = 1; i < n+1; i++)
        {
            v[i] = v[i-1] + x[i-1];
        }
        sort(v.begin(), v.end());
        int h = v[n];
        return h;
    }
};
