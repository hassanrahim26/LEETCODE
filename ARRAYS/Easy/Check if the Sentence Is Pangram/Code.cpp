/*
PROBLEM LINK:- https://leetcode.com/problems/check-if-the-sentence-is-pangram/
*/

class Solution {
public:
    bool checkIfPangram(string str) {
        int n = str.size();
        vector v(26,0);
        
        for(int i = 0; i < n; i++)
        {
            v[str[i]-'a']++;
        }
        
        for(int i = 0; i < v.size(); i++)
        {
            if(v[i] == 0)
                return false;
        }
    return true;
    }
};
