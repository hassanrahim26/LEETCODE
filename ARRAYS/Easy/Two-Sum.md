## [Two Sum](https://leetcode.com/problems/two-sum/)

* **C++**
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for(int i = 0; i < nums.size(); i++)
        {
            auto it = mp.find(target - nums[i]);
            if(it != mp.end())  
                return {it->second, i};
            else
                mp.insert({nums[i], i});
        }
        
        return {-1, -1};
    }
};
```

* **Python**
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[target - nums[i]] = i
            else:
                return mp[nums[i]], i

        return -1, -1
```
