/*
PROBLEM LINK:- https://leetcode.com/problems/create-target-array-in-the-given-order/
*/

class Solution {
public:
    vector<int> createTargetArray(vector<int>& v1, vector<int>& v2) {
        int n = v2.size();
        vector<int> r;
        for(int i = 0; i < n; i++)
        {
            r.insert(r.begin() + v2[i], v1[i]);
        }
        return r;
    }
};
