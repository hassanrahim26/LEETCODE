/*
PROBLEM LINK:- https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
*/

class Solution {
public:
    int countNegatives(vector<vector<int>>& v) {
        int n = v.size(), m = v[0].size();
        int i = n - 1, j = 0, count = 0;
        
        while(i >= 0 && i < n && j >= 0 && j < m)
        {
            if(v[i][j] < 0)
            {
                count += m - j;
                i -= 1;
            }
            
            else
            {
                j += 1;
            }
        }
        
        return count;
    }
};
