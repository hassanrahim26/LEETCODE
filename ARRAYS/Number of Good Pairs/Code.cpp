/*
PROBLEM LINK:- https://leetcode.com/problems/number-of-good-pairs/
*/

class Solution {
public:
    int numIdenticalPairs(vector<int>& v) {
        int c = 0, n = v.size();
        for(int i = 0; i < n; i++)
        {
            for(int j = 1; j < n; j++)
            {
                if(i<j && v[i] == v[j])
                {
                    c++;
                }
            }
        }
        return c;
    }
};
