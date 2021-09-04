/*
PROBLEM LINK:- https://leetcode.com/problems/matrix-diagonal-sum/
*/

class Solution {
public:
    int diagonalSum(vector<vector<int>>& v) {
        int n = v.size();
        int s = 0;
        
        for(int i = 0; i < n; i++)
        {
            s += v[i][i];
            if(i != n-i-1)
                s += v[i][n-i-1];
        }
        
        return s;
    }
};
