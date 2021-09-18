/*
PROBLEM LINK:- https://leetcode.com/problems/height-checker/
*/

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int n = heights.size();
        vector<int> expected(heights.begin(), heights.end());
        sort(expected.begin(), expected.end());
        int c = 0;
        for(int i = 0; i < n; i++)
        {
            if(heights[i] != expected[i])
            {
                c++;
            }
        }
        return c;
    }
};
