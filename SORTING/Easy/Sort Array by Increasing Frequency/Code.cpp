/*
PROBLEM LINK:- https://leetcode.com/problems/sort-array-by-increasing-frequency/
*/

class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(int x: nums)
            mp[x]++;
        sort(nums.begin(), nums.end(), [&](int a, int b){
            return mp[a] == mp[b] ? a > b : mp[a] < mp[b];
        });
        return nums;
    }
};
