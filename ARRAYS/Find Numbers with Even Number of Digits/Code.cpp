/*
PROBLEM LINK:- https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
*/

class Solution {
public:
    int findNumbers(vector<int>& v) {
        int n = v.size();
        int c, d = 0;
        for(int i = 0; i < n; i++)
        {
            c = 0;
            while(v[i] > 0)
            {
                v[i] /= 10;
                c++;
            }
            
            if(c % 2 == 0)
                d++;
        }
        return d;
    }
};
