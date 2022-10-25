/*
PROBLEM LINK:- https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
*/

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        return reduce(word1.cbegin(), word1.cend()) == reduce(word2.cbegin(), word2.cend());        
    }
};
