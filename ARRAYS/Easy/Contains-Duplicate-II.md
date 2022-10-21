## [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

* **C++**
```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        int i = 0, j = 0;
        
        for(; j < nums.size(); j++)
        {
            if(j > k)
                mp[nums[i++]]--;
            
            if(mp[nums[j]] > 0)
                return true;
            
            mp[nums[j]]++;
        }
        
        return false;
    }
};
```

* **PYTHON**
```py
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
        return False
```
