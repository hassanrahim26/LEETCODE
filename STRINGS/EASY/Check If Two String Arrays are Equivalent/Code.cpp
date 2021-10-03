/*
PROBLEM LINK:- https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
*/

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s1, s2;
        for(auto a : word1) s1 += a;
        for(auto b : word2) s2 += b;
        return s1 == s2;
    }
};
