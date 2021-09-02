/*
PROBLEM LINK:- https://leetcode.com/problems/contains-duplicate/
*/

class Solution {
public:
    bool containsDuplicate(vector<int>& v) {
        unordered_set<int> v_set(v.begin(), v.end());
        return v_set.size() != v.size();
    }
};
