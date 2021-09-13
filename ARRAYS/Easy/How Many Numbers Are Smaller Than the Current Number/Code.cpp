/*
PROBLEM LINK:- https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
*/

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& v) {
        int n = v.size();
        vector<int> r;
        
        for(int i = 0; i < n; i++) 
        {
            int c = 0;
            for(int j = 0; j < n; j++) 
            {
                if(j!=i and v[j] < v[i])
                    c++;
            }
            r.push_back(c);
        }
        return r;
    }
};
