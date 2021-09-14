/*
PROBLEM LINK:- https://leetcode.com/problems/transpose-matrix/
*/

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& v) {
        int m = v.size(), n = v[0].size();
        vector<vector<int>> ans(n,vector(m,0));
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++)
                ans[i][j] = v[j][i];
        }
        return ans;
    }
};
