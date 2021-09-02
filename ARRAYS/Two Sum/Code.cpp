/*
PROBLEM LINK:- https://leetcode.com/problems/two-sum/
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& v, int x) {
        int n = v.size();
        vector<int> r;
        for(int i = 0; i < n; i++)
        {
            for(int j = i+1; j < n; j++)
            {
                if(i != j and v[i]+v[j] == x)
                {
                    r.push_back(i);
                    r.push_back(j);
                }
            }
        }
        return r;
    }
};
