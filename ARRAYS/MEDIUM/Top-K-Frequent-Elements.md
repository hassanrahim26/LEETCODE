## [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

* **C++**
```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        
        for(auto x: nums)
            mp[x]++;
       
        vector<vector<int>> buckets(nums.size()+1);
        for(auto [a, b] : mp)
            buckets[b].push_back(a);
    
        vector<int> ans;
        for(int i = nums.size(); k; i--)
        {
            for(auto x: buckets[i])
            {
                ans.push_back(x);
                k--;
            }
        }
        
        return ans;
    }
};
```
